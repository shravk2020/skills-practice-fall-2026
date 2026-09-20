import pytest
from starter import Account, SavingsAccount


def test_init_sets_owner_and_balance():
    acc = Account("Alice", 100)
    assert acc.owner == "Alice"
    assert acc.balance == 100


def test_init_default_balance_is_zero():
    acc = Account("Bob")
    assert acc.balance == 0


def test_deposit():
    acc = Account("Alice", 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw_success():
    acc = Account("Alice", 100)
    acc.withdraw(40)
    assert acc.balance == 60


def test_withdraw_insufficient_funds():
    acc = Account("Alice", 100)
    with pytest.raises(ValueError):
        acc.withdraw(200)


def test_bank_name_is_shared_across_instances():
    a = Account("Alice", 100)
    b = Account("Bob", 50)
    assert a.bank_name == "Terp Bank"
    assert b.bank_name == "Terp Bank"
    Account.bank_name = "New Bank"
    assert a.bank_name == "New Bank"
    assert b.bank_name == "New Bank"
    Account.bank_name = "Terp Bank"  # reset for other tests


def test_setting_bank_name_on_one_instance_does_not_affect_others():
    a = Account("Alice", 100)
    b = Account("Bob", 50)
    a.bank_name = "Alice's Personal Bank"
    assert a.bank_name == "Alice's Personal Bank"
    assert b.bank_name == "Terp Bank"


def test_from_string_classmethod():
    acc = Account.from_string("Charlie:250.0")
    assert isinstance(acc, Account)
    assert acc.owner == "Charlie"
    assert acc.balance == 250.0


def test_is_valid_amount_staticmethod():
    assert Account.is_valid_amount(10) is True
    assert Account.is_valid_amount(-5) is False
    # staticmethods are callable on instances too, with no self passed:
    acc = Account("Alice", 100)
    assert acc.is_valid_amount(10) is True


def test_savings_account_is_an_account():
    savings = SavingsAccount("Alice", 500, interest_rate=0.02)
    assert isinstance(savings, Account)
    assert savings.owner == "Alice"
    assert savings.balance == 500
    assert savings.interest_rate == 0.02


def test_savings_account_default_interest_rate():
    savings = SavingsAccount("Alice", 500)
    assert savings.interest_rate == 0.01


def test_savings_account_withdraw_enforces_minimum_balance():
    savings = SavingsAccount("Alice", 500)
    with pytest.raises(ValueError):
        savings.withdraw(450)  # would leave 50, below the $100 minimum


def test_savings_account_withdraw_succeeds_above_minimum():
    savings = SavingsAccount("Alice", 500)
    savings.withdraw(300)  # leaves 200, above the $100 minimum
    assert savings.balance == 200


def test_savings_account_still_raises_on_insufficient_funds():
    savings = SavingsAccount("Alice", 500)
    with pytest.raises(ValueError):
        savings.withdraw(10000)
