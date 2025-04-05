import pytest
class BankAccount:
    def __init__(self, owner,balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount
        print(f"Баланс пополнен на сумму: {amount}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        print(f"С вашего счёта списано: {amount}")

    def get_balance(self):
        return self.__balance
    def test_positive_balance(self):
        final_balance= self.get_balance()
        assert final_balance > 0, "Баланс <= 0"

class SavingsAccount(BankAccount):
    def __init__(self, owner ,balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        if self.get_balance() > 0:
            interest = self.get_balance() * self.interest_rate
            self.deposit(interest)
            print(f"Начислено процентов: {interest} на остаток по счёту")

class CheckingAccount(BankAccount):
    def __init__(self, owner ,balance=0):
        super().__init__(owner , balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        self._BankAccount__balance -= amount
        print(f"С вашего счёта списано: {amount} (овердрафт разрешен)")

savings_account_1=SavingsAccount("Ильич")
savings_account_1.deposit(500)
savings_account_1.withdraw(100)
savings_account_1.apply_interest()





