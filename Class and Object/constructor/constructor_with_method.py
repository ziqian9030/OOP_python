class Information:
    def __init__(self,id,name,age,gender):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender

    def output(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

    def subject(self,math,english,khmer):
        avg = (math+english+khmer)/3

        print("Math:",math)
        print("English:",english)
        print("Khmer:",khmer)
        print("Average",avg)
        if avg >50:
            print("Pass")
        else:
            print("Fail")
        return avg

    # def check(self):
    #     if self.avg > 50:
    #         print("Pass")
    #     else:
    #         print("Fail")



id = int(input("Enter ID: "))
name = input("Enter name: ")
age = int(input("Enter Age: "))
gender = input("Enter gender: ")

infomration1 = Information(id,name,age,gender)
infomration1.output()

math = int(input("Enter math score: "))
english = int(input("Enter English score: "))
khmer = int(input("Enter Khmer score: "))
infomration1.subject(math,english,khmer)

# infomration1.check()