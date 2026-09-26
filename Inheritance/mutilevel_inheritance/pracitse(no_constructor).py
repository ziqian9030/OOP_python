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






order = Onlineorder()
order.inputorder()
os.system('cls')
order.showorder()

order.search()
