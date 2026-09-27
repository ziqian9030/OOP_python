import os
class Person:
    def inputperson(self):
        self.id=int(input("Enter ID: "))
        self.age=int(input("Enter Age: "))
        self.name=input("Enter Name: ")

    def printperson(self):
        print("----Infor----")
        print("ID: ",self.id)
        print("Age: ",self.age)
        print("Name: ",self.name)

class Doctor(Person):
    def inputdoc(self):
        self.spec=input("Enter doctor specialization: ")
        self.ex=int(input("Enter doctor experience: "))

    def outputdoc(self):
        print("\n----Doctor----")
        print("Specialization: ",self.spec)
        print("Experience: ",self.ex)

class Nurse(Person):
    def inputnures(self):
        self.dep=input("Enter Nurse department: ")
        self.shift=input("Enter Shift: ")

    def outputnurse(self):
        print("\n----Nurse----")
        print("Department: ",self.dep)
        print("Shift: ",self.shift)

class Team(Doctor,Nurse):
    def inputteam(self):
        self.inputperson()
        self.inputdoc()
        self.inputnures()
        self.teamname=input("Enter team name: ")
        self.hop=input("Enter hospital name: ")
        self.room=input("Enter room: " )

    def outputeam(self):
        self.printperson()
        self.outputdoc()
        self.outputnurse()
        print("\n----Team----")
        print("Team Name: ",self.teamname)
        print("Hospital: ",self.hop)
        print("Room: ",self.room)


obj = Team()

obj.inputteam()
os.system('cls')
obj.outputeam()