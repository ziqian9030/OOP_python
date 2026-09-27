import os
class Farmworker:
    def input1(self):
        self.id=int(input("Enter Farm worker ID: "))
        self.name=input("Enter Farm worker name: ")
        self.age=int(input("Enter Farm worker age: "))

    def output1(self):
        print("----Farm Worker----")
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Age: ",self.age)

class Cropmanager(Farmworker):
    def input2(self):
        self.cropname=input("Enter crop name: ")
        self.area=input("Enter Area: ")

    def output2(self):
        print("\n----Crop Manager----")
        print("Crop name: ",self.cropname)
        print("Crop area: ",self.area)

class Animalmanager(Farmworker):
    def input3(self):
        self.type=input("Enter animal type: ")
        self.count=int(input("Enter number the quantity: "))

    def output3(self):
        print("\n----Farm worker----")
        print("Animal type: ",self.type)
        print("Animal quantity: ",self.count)

class FarmManager(Cropmanager,Animalmanager):
    def input4(self):
        self.input1()
        self.input2()
        self.input3()
        self.name2=input("Enter Farm manager name: ")
        self.location=input("Enter Farm manager location: ")

    def output4(self):
        self.output1()
        self.output2()
        self.output3()
        print("\n----Farm Manager----")
        print("Name: ",self.name2)
        print("Location: ",self.location)

obje1 = FarmManager()

obje1.input4()
os.system('cls')
obje1.output4()