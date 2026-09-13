class Bank:
    def __init__(self,name,balance,password):
        self.name=name
        self.balance=balance
        self.password=password

    def output(self):
        print("Name:",self.name)
        print("Balance:",self.balance)
        print("Password:",self.password)

    def withdraw(self, balance,withdraw):
        balance -= withdraw
        print("Balance after withdraw:",balance)



name=input("Enter Name: ")
Balance=int(input("Enter Balance: "))
password=input("Enter Password: ")
bank1 = Bank(name,Balance,password)
bank1.output()

withdraw1 = int(input("How much you want to take: "))
bank1.withdraw(Balance,withdraw1) 
