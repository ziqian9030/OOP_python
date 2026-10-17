import os
class Vehicle:
    def input1(self):
        self.brand=input("Enter brand: ")
        self.model=input("Enter model: ")
        self.year=input("Enter year: ")

    def output1(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Year: ",self.year)

class Car(Vehicle):
    def input2(self):
        self.input1()
        self.fuel=input("Enter fuel type: ")

    def output2(self):
        self.output1()
        print("Fuel type: ",self.fuel)

class Moto(Car):
    def input3(self):
        self.input2()
        self.enginesize=input("Enter engine size: ")

    def output3(self):
        self.output2()
        print("Engine size: ", self.enginesize)

obje1=Moto()
obje1.input3()
os.system('cls')

obje1.output3()