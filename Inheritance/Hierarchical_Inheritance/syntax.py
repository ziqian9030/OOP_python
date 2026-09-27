import os
class Animal:
    def inputaniaml(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
        self.color=input("Enter color: ")

    def printanimal(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Color: ",self.color)

class Dog(Animal):
    def inputdog(self):
        self.inputaniaml()
        self.breed=input("Enter breed: ")

    def outputdog(self):
        self.printanimal()
        print("Breed: ",self.breed)

class Cat(Animal):
    def inputcat(self):
        self.inputaniaml()
        self.legs=int(input("Enter how many legs: "))

    def outputcat(self):
        self.printanimal()
        print("Legs: ",self.legs)

obj1= Dog()
obj2= Cat()
print("---Enter dog information---")
obj1.inputdog()
os.system('cls')
obj1.outputdog()

print("---Enter cat information---")
obj2.inputcat()
os.system('cls')
obj2.outputcat()