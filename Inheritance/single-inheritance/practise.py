class Employee:
    def __init__(self,id,name,age,gender,apartment,salary):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
        self.apartment=apartment
        self.salary=salary

    def showinfor(self):
        print("----- Employees -----")
        print("ID:",self.id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Apartment:",self.apartment)
        print("Salary:",self.salary)

    def cal(self):
        salary = self.salary*12
        print("Annual salary: ",salary)

class Developer(Employee):
    def __init__(self, id, name, age, gender, apartment, salary,lanaguae,experience):
        super().__init__(id, name, age, gender, apartment, salary)
        self.lanaguae=lanaguae
        self.experience=experience

    def show(self):
        print("----- Developer -----")
        print("Programming language: ",self.lanaguae)
        print("Experience: ",self.experience)

id = int(input("Enter ID: "))
Name = input("Enter Name: ")
Age = input("Enter Age: ")
Gender = input("Enter Gender: ")
apartement = input("Enter Apartement: ")
salary = int(input("Enter Salary: "))
language = input("Enter programming language: ")
ex = input("Enter year of experience: ")

dev = Developer(id,Name,Age,Gender,apartement,salary,language,ex)
dev.show()
dev.showinfor()
dev.cal()