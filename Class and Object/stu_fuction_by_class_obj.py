class Student:
    name = ""
    age = ""

    def add_student(self):
        self.name = input(" Put student name: ")
        self.age = input(" Put student age: ")

    def show_student(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

    def search_stu(self):
        search = input(" Enter student name to search: ")
        if search == self.name:
            print("Name:", self.name)
            print("Age:", self.age)
        else:
            print(" No student has been found")

student1 = Student()

student1.add_student()

student1.show_student()

student1.search_stu()
