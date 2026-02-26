class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Сумма пополнения должна быть больше 0")
            return
        self.balance += amount
        print(f"Пополнение: +{amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть больше 0")
            return
        if amount > self.balance:
            print(f"Недостаточно средств. Баланс: {self.balance}")
            return
        self.balance -= amount
        print(f"Снятие: -{amount}. Баланс: {self.balance}")


acc1 = BankAccount("AZ1001", "Айшан", 200)
acc2 = BankAccount("AZ1002", "Марьям", 50)
acc3 = BankAccount("AZ1003", "Мелисса")

acc1.deposit(100)
acc1.withdraw(50)

acc2.withdraw(70)
acc2.deposit(30)
acc2.withdraw(70)

acc3.deposit(20)
acc3.withdraw(5)