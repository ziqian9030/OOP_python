class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showperson(self):
        print(" Name: ",self.name)
        print(" Age: ", self.age)

class Student(Person):
    def __init__(self, name, age,id,grade):
        Person.__init__(self,name, age)
        self.id=id
        self.grade=grade

    def showstudent(self):
        print("ID: ",self.id)
        print("Grade: ",self.grade)

class Unistudent(Student):
    def __init__(self, name, age, id, grade,major):
        Student.__init__(self,name, age, id, grade)
        self.major=major

    def showUnistudent(self):
        self.showperson()
        self.showstudent()
        print("Major: ",self.major)

name=input("Enter name: ")
age=input("Enter age: ")
id=input("Enter id: ")
grade=input("Enter grade: ")
major=input("Enter major: ")
unistudent = Unistudent(name,age,id,grade,major)


unistudent.showUnistudent()