class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def showinfor(self):
        print("----- Employees -----")
        print("ID:",self.id)
        print("Name:",self.name)
        print("Salary:",self.salary)

    def cal(self):
        salary = self.salary*12
        print("Annual salary: ",salary)

class Developer():
    def __init__(self,lanaguae,experience):
        self.lanaguae=lanaguae
        self.experience=experience

    def show(self):
        print("----- Developer -----")
        print("Programming language: ",self.lanaguae)
        print("Experience: ",self.experience)

class Senior(Employee,Developer):
    def __init__(self, id, name, salary,experience,project,lanaguae):
        Employee. __init__(self,id,name,salary)
        Developer.__init__(self,lanaguae,experience)
        self.experience=experience
        self.project=project

    def show2(self):
        print("----- Senior developer -----")
        print("Year of experience: ",self.experience)
        print("Project: ",self.project)



id = int(input("Enter ID: "))
Name = input("Enter Name: ")
salary = int(input("Enter Salary: "))
ex = input("Enter year of experience: ")
language = input("Enter programming language: ")
proj = input("Enter Project: ")

senior1 = Senior(id,Name,salary,ex,language,proj)

senior1.showinfor()
senior1.show()
senior1.show2()
senior1.cal()
