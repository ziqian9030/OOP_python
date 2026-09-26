import os
class Food:
    def inputfood(self):
        self.food=input("Enter food: ")
        self.price=input("Enter price: ")

    def showfood(self):
        print("Food: ",self.food)
        print("Price: ",self.price)

class Delivery(Food):
    def inputdelivery(self):
        self.inputfood()
        self.address=input("Enter adresse: ")
        self.fee=input("Enter fee: ")

    def showdelivery(self):
        self.showfood()
        print("Delivery address: ",self.address)
        print("Delivery fee: ",self.fee)

class Onlineorder(Delivery):
    def inputorder(self):
        self.inputdelivery()
        self.id=int(input("Enter ID: "))
        self.name=input("Enter name: ")

    def showorder(self):
        self.showdelivery()
        print("Order ID: ",self.id)
        print("Order name: ",self.name)

    def search(self):
        search1=int(input("\n Enter ID to search: "))
        if search1 == self.id:
            self.showorder()
        else:
            print(" Order not found")
            
while True:

    order1=Onlineorder()
    print(" ----- Menu -----")
    print("1. Order food ")
    print("2. Show your order ")
    print("3. Search order")
    print("4. Exit")

    chice = int(input("Enter your choice: "))
    match chice:
        case 1:
            order1.inputorder()
        case 2:
            order1.showdelivery()
        case 3:
            order1.search()
        case 4:
            print(" Thank you")
            break
        case _:
            print("Invalid option")
            break
