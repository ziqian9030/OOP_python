class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showinfor(self):
        print("----- Basic infor -----")
        print("Name: ",self.name)
        print("Age: ",self.age)

class Employees:
    def __init__(self,id,salary):
        self.id=id
        self.salary=salary

    def show(self):
        print("----- Employee -----")
        print("Employee ID: ",self.id)
        print("Salary: ",self.salary)

class Manager(Parent,Employees):
    def __init__(self, name, age,id,salary,departement):
        Parent.__init__(self,name,age)
        Employees.__init__(self,id,salary)
        self.dep=departement

    def final_show(self):
        print("----- Manager -----")
        print("Departement: ",self.dep)


name=input("Enter Name: ")
age=input("Enter Age: ")
id=input("Enter ID: ")
salary=input("Enter Salary: ")
dep=input("Enter Departement: ")

manager1=Manager(name,age,id,salary,dep)
manager1.showinfor()
manager1.show()
manager1.final_show()