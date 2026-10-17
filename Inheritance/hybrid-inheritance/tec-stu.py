import os
class Person:
    def input_person(self):
        self.id=input("Enter ID: ")
        self.name=input("Enter Name: ")
        self.age=input("Enter Age: ")

    def output_person(self):
        print("----- Infor -----")
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Age: ",self.age)

class Student(Person):
    def input_stu(self):
        self.grade =input("Enter grade: ")
        self.major =input("Enter major: ")

    def output_stu(self):
        print("\n-----Student-----")
        print("Grade: ",self.grade)
        print("Major: ",self.major)

class Teacher(Person):
    def input_teach(self):
        self.subj=input("Enter subject: ")
        self.exp=input("Enter experience: ")

    def output_teach(self):
        print("\n-----Teacher-----")
        print("Subejct: ",self.subj)
        print("Experience: ",self.exp)

class School_team(Student,Teacher):
    def input_team(self):
        self.input_person()
        self.input_stu()
        self.input_teach()
        self.teamname=input("Enter team name: ")
        self.acitivy=input("Enter activity: ")
        self.room=input("Enter room: ")

    def output_team(self):
        self.output_person()
        self.output_stu()
        self.output_teach()
        print("\n-----School team-----")
        print("Team name: ",self.teamname)
        print("Activity: ",self.acitivy)
        print("Room: ",self.room)

obejct1 = School_team()
obejct1.input_team()
os.system('cls')
obejct1.output_team()