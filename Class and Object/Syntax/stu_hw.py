
class Student:
    id = ""
    name = ""
    age = ""
    gender = ""
    average = ""
    def input(self):
        self.id =int(input(" Enter your ID: "))
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
        self.gender=input("Enter gender: ")
        self.average=int(input(" Enter your average score: "))

    def show(self):
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Average: ",self.average)

   
student1 = Student()
student1.input()
student1.show()
# fuc.input()
# fuc.show()