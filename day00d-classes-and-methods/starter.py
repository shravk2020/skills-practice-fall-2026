class Account:
    """TODO: implement.

    - class attribute: bank_name = "Terp Bank"
    - __init__(self, owner, balance=0): store both.
    - deposit(self, amount): add amount to balance.
    - withdraw(self, amount): raise ValueError("insufficient funds") if
      amount > self.balance, otherwise subtract amount from balance.
    - from_string(cls, data): a classmethod. data looks like "Alice:100.0".
      Parse it and return a new Account.
    - is_valid_amount(amount): a staticmethod. Return True if amount > 0,
      else False. Takes neither self nor cls.
    """
    pass


class SavingsAccount(Account):
    """A kind of Account with an interest_rate and a stricter withdraw rule.

    TODO: implement.

    - __init__(self, owner, balance=0, interest_rate=0.01): call
      super().__init__(owner, balance), then store interest_rate.
    - withdraw(self, amount): raise ValueError("savings must keep a $100
      minimum balance") if (self.balance - amount) < 100. Otherwise, do the
      actual withdrawal by calling super().withdraw(amount) -- don't
      duplicate Account's logic here.
    """
    pass
