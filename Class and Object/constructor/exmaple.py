class Employee:
    def __init__(self,id,name,gender,position,salary,exp):
        self.id=id
        self.name=name
        self.gender=gender
        self.position=position
        self.salary=salary
        self.exp=exp

    def show(self):
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Gender: ",self.gender)
        print("Position: ",self.position)
        print("Salary: ",self.salary)
        print("Year of Experience: ",self.exp)

employee1 = Employee(111,"ziqian","M","Manager","20milion per year","15 years")
employee1.show()