class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def check_cash(self):
        print(f"Your balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Account replenishment: {amount} . You have {self.balance}")


    def withdrawal(self, amount):
        if amount > self.balance:
            print("Withdrawal is not possible. Balance is low")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from the deposit. Balance is {self.balance}")

ba1 = Account("Nursultan")
ba2 = Account("Kerey")

ba1.check_cash()
ba1.withdrawal(69)
ba1.deposit(1991)
ba1.withdrawal(526)