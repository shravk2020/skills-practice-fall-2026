# Day 0d — Classes & Method Construction

## Why this matters
Day 3 covered `@property` and dunder methods, but skipped past the actual
mechanics of class construction: what `self` really is, the difference
between an attribute that belongs to *one instance* vs. one shared by *every
instance of the class*, and the three kinds of methods a class can have
(instance, class, static) — each with a different purpose. This is the stuff
that makes Pydantic models, SQLModel/ORM rows, and every class you'll write
from here on actually make sense instead of feeling like a template you
copy-paste.

## Where you'll actually use this
- **Pydantic models (Week 3)** and **SQLModel rows (Week 5)** are classes —
  understanding instance attributes and `__init__` is what makes those
  frameworks legible instead of magic.
- **`@classmethod` as an alternate constructor** (`MyClass.from_string(...)`,
  `MyClass.from_dict(...)`) is an extremely common real-world pattern —
  you'll see it constantly in libraries you use.
- **Inheritance + `super()`** is how you'll model "a Savings account is a
  kind of Account, but with extra rules" — a shape that shows up constantly
  in real domain modeling, and is a very standard interview topic.

## Concepts in depth

### `self` and instance attributes
```python
class Dog:
    def __init__(self, name):
        self.name = name    # an INSTANCE attribute -- belongs to this one Dog

fido = Dog("Fido")
rex = Dog("Rex")
fido.name   # "Fido"
rex.name    # "Rex" -- separate storage, even though it's the same class
```
`self` is just the instance the method was called on — Python passes it in
automatically. `self.name = name` stores `name` *on that specific object*.
Every instance gets its own independent copy.
Docs: https://docs.python.org/3/tutorial/classes.html#instance-objects

### Class attributes (shared across every instance)
```python
class Dog:
    species = "Canis familiaris"   # a CLASS attribute -- shared by ALL dogs

    def __init__(self, name):
        self.name = name           # instance attribute

fido = Dog("Fido")
rex = Dog("Rex")
fido.species   # "Canis familiaris"
Dog.species = "changed"
fido.species   # "changed"  -- ALL instances see the change
rex.species    # "changed"  -- same here
```
**The gotcha:** if you try to *reassign* a class attribute through an
instance (`fido.species = "just fido's"`), Python doesn't change the shared
value — it creates a **new instance attribute** on `fido` that shadows the
class attribute, and only `fido` sees the new value. This is genuinely
confusing the first time you hit it — today's tests make you observe it
directly.
Docs: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

### Instance methods vs. `@classmethod` vs. `@staticmethod`
```python
class Account:
    bank_name = "Terp Bank"       # class attribute

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):             # INSTANCE method: needs self,
        self.balance += amount             # reads/writes this instance's data

    @classmethod
    def from_string(cls, data):            # CLASSMETHOD: needs cls (the
        owner, balance = data.split(":")   # class itself), not any instance.
        return cls(owner, float(balance))  # Common use: alternate constructor.

    @staticmethod
    def is_valid_amount(amount):           # STATICMETHOD: needs neither self
        return amount > 0                  # nor cls. Just a utility function
                                            # that's grouped inside the class
                                            # because it's conceptually related.
```
| Kind | First parameter | Called via | Use it for |
|---|---|---|---|
| instance method | `self` | `instance.method()` | reading/writing this specific object's data |
| `@classmethod` | `cls` | `ClassName.method()` (or on an instance) | alternate constructors, anything that needs the class itself, not one instance |
| `@staticmethod` | (neither) | `ClassName.method()` (or on an instance) | a helper function that's related to the class but doesn't need instance or class data |

Docs: https://docs.python.org/3/library/functions.html#classmethod and
https://docs.python.org/3/library/functions.html#staticmethod

### Inheritance and `super()`
```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)     # let Account set up owner/balance
        self.interest_rate = interest_rate   # then add what's new

    def withdraw(self, amount):
        if self.balance - amount < 100:
            raise ValueError("savings must keep a $100 minimum balance")
        super().withdraw(amount)             # reuse Account's actual logic
```
`class SavingsAccount(Account):` means every `SavingsAccount` *is an*
`Account` too, and starts with everything `Account` has. `super()` lets a
subclass call the parent class's version of a method — here,
`SavingsAccount.withdraw` adds an *extra* rule on top, then delegates the
actual withdrawal logic back to `Account.withdraw` instead of duplicating
it. **When to use inheritance:** when "B is a kind of A, with some
differences" is genuinely true of your data. Don't reach for it just to
share a couple of unrelated helper functions — that's what a plain function
or a separate helper class is for.
Docs: https://docs.python.org/3/tutorial/classes.html#inheritance

## The task
Open `starter.py`. Build:
1. `Account` — `__init__(self, owner, balance=0)`, a class attribute
   `bank_name = "Terp Bank"`, instance methods `deposit(amount)` and
   `withdraw(amount)` (raises `ValueError` if `amount > self.balance`), a
   classmethod `from_string(cls, data)` that parses `"owner:balance"` into a
   new `Account`, and a staticmethod `is_valid_amount(amount)` returning
   whether `amount > 0`.
2. `SavingsAccount(Account)` — same constructor plus `interest_rate=0.01`,
   using `super().__init__(...)`. Overrides `withdraw` to enforce a $100
   minimum balance *in addition to* the base insufficient-funds check, by
   calling `super().withdraw(amount)` for the actual logic.

## Run it
```bash
cd day00d-classes-and-methods
pytest -v
```

## Common pitfalls
- Forgetting `self` as the first parameter of an instance method — Python
  will pass the instance in regardless, so a method defined as
  `def deposit(amount):` (missing `self`) breaks with a confusing
  "too many arguments" error the moment you call it normally.
- Calling `super().__init__(...)` with the wrong arguments, or forgetting
  it entirely — if you forget it in `SavingsAccount.__init__`, `owner` and
  `balance` never get set at all.
- Mutating a class attribute that's a *mutable* object (like a list) through
  one instance affects every instance, because there's only ever one shared
  list — this is the same trap as Day 0a's mutable default argument, showing
  up again in a different spot.

## Stretch goal (optional)
Add `__repr__` to `Account` (same idea as Day 3) so `print(account)` shows
something useful. Then add a `CheckingAccount(Account)` with an
`overdraft_limit` that allows `withdraw` to take the balance negative, down
to `-overdraft_limit`, instead of raising. This gives you two different
subclasses of the same base class with genuinely different `withdraw` rules
— the actual point of inheritance + overriding.

## Further reading
- Python's full classes tutorial (the best single source for all of today):
  https://docs.python.org/3/tutorial/classes.html
- Real Python on classmethod vs staticmethod (good if the table above isn't
  clicking yet): https://realpython.com/instance-class-and-static-methods-demystified/
