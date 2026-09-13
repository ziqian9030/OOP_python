class Student:
    def input(self):
        self.id = int(input("Enter ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gneder: ")
        self.math = int(input("Enter math score: "))
        self.english = int(input("Enter English score: "))

    def output(self):
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Math score: ",self.math)
        print("English score: ",self.english)

    def total(self):
        self.total = self.english+self.math
        print("Total score: ",self.total)

    def avg(self):
        self.avg = (self.english+self.math)/2
        print("Averge score: ",self.avg)

student1 = Student()
student1.input()
student1.output()
student1.total()
student1.avg()