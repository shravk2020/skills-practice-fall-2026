class Account:
    bank_name = "Terp Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    @classmethod
    def from_string(cls, data):
        owner, balance = data.split(":")
        return cls(owner, float(balance))

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if (self.balance - amount) < 100:
            raise ValueError("savings must keep a $100 minimum balance")
        super().withdraw(amount)
