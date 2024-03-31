class BankAccount:
    def __init__(self, account_number, balance, name, account_type, interest_rate=0.0):
        self.__account_number = account_number
        self.__balance = balance
        self.__name = name
        self.__account_type = account_type
        self.__interest_rate = interest_rate

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("จำนวนเงินถอนต้องมากกว่า 0")
        if amount > self.__balance:
            raise ValueError("ยอดเงินถอนเกินจำนวนเงินคงเหลือ")
        self.__balance -= amount

    def get_balance(self):

        return self.__balance

    def get_account_number(self):

        return self.__account_number

    def get_name(self):

        return self.__name

    def get_account_type(self):

        return self.__account_type

    def calculate_interest(self):

        if self.__account_type in ("SAVINGS", "CHECKING"):
            return self.__balance * self.__interest_rate
        else:
            raise ValueError("ประเภทบัญชีไม่ถูกต้อง")

    def transfer_money(self, to_account, amount):

        if amount <= 0:
            raise ValueError("จำนวนเงินโอนต้องมากกว่า 0")
        if amount > self.__balance:
            raise ValueError("ยอดเงินโอนเกินจำนวนเงินคงเหลือ")
        self.__balance -= amount
        to_account.deposit(amount)

account1 = BankAccount(630910305, 15000, "Kittamate Jangsanit", "SAVINGS", 0.015)
account2 = BankAccount(630910305, 10000, "Kittamate Jangsanit", "CHECKING", 0.0)

account1.deposit(5000)
account2.deposit(2000)

account1.withdraw(2000)
account2.withdraw(1000)

print(f"ยอดเงินคงเหลือในบัญชี {account1.get_account_number()} : {account1.get_balance()}")
print(f"ยอดเงินคงเหลือในบัญชี {account2.get_account_number()} : {account2.get_balance()}")

print(f"ดอกเบี้ยของบัญชี {account1.get_account_number()} : {account1.calculate_interest()}")
print(f"ดอกเบี้ยของบัญชี {account2.get_account_number()} : {account2.calculate_interest()}")

account1.transfer_money(account2, 1000)

print(f"ยอดเงินคงเหลือในบัญชี {account1.get_account_number()} : {account1.get_balance()}")
print(f"ยอดเงินคงเหลือในบัญชี {account2.get_account_number()} : {account2.get_balance()}")