from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def _is_account_valid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            not self._is_account_valid(account1)
            or not self._is_account_valid(account2)
            or self.balance[account1 - 1] < money
        ):
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_account_valid(account):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_account_valid(account) or self.balance[account - 1] < money:
            return False

        self.balance[account - 1] -= money
        return True


def test_Bank():
    bank = Bank([10, 100, 20, 50, 30])
    assert bank.withdraw(3, 10)
    assert bank.transfer(5, 1, 20)
    assert bank.deposit(5, 20)
    assert not bank.transfer(3, 4, 15)
    assert not bank.withdraw(10, 50)
