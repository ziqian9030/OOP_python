class Bank:
    def __init__(self,number,name,type,balance):
        self.number=number
        self.name=name
        self.type=type
        self.balance=balance

    def infor(self):
        print("----- Banking -----")
        print(" Account number: ",self.number)
        print(" Name: ",self.name)
        print(" Account type: ",self.type)
        print(" Account balance: ",self.balance)

    def deposite(self):
        dep = int(input("How much do you want deposite: "))
        self.balance = self.balance+dep
        print(" New Balance: ",self.balance)

    def withdraw(self):
        draw = int(input("How much do you want to withdraw: "))
        self.balance = self.balance-draw
        print("New balance: ",self.balance)

class Saving(Bank):
    def __init__(self, number, name, type, balance,interest):
        super().__init__(number, name, type, balance)
        self.interest=interest

    def show(self):
        print("----- Saving account -----")
        print("Interest rate: ",self.interest)

acc_num = input("Enter account number: ")
acc_name = input("Enter account name: ")
type = input("Enter account type: ")
balance = int(input("Enter account balance: "))
rate = int(input("Enter interest rate: "))

saving1 = Saving (acc_num,acc_name,type,balance,rate)
saving1.infor()
saving1.show()
saving1.deposite()
saving1.withdraw()
    
