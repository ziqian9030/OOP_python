import os
class Food:
    def __init__(self,food,price):
        self.food=food
        self.price=price

    def showfood(self):
        print("Food: ",self.food)
        print("Price: ",self.price)

class Delivery(Food):
    def __init__(self, food, price,address,fee):
        Food.__init__(self,food, price)
        self.address=address
        self.fee=fee

    def showdelivery(self):
        self.showfood()
        print("Delivery address: ",self.address)
        print("Delivery fee: ",self.fee)

class Onlineorder(Delivery):
    def __init__(self, food, price, address, fee,id,name):
        Delivery.__init__(self,food, price, address, fee)
        self.id=id
        self.name=name

    def showorder(self):
        self.showdelivery()
        print("Order ID: ",self.id)
        print("Order name: ",self.name)

food=input("Order your food: ")
price=input("Enter your Price: ")
adress=input("Enter your Adressee: ")
fee=input("Enter your Fee: ")
id=input("Enter your ID: ")
name=input("Enter your Name: ")
os.system('cls')

order = Onlineorder(food,price,adress,fee,id,name)
order.showorder()