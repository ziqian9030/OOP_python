class Dog:
    name = ""
    color = ""

    def sound(self):
        print("Bark")


dog1 = Dog()

dog1.name = input(" Enter dog name: ")
dog1.color = input(" Enter dog color: ")
print("Name: ",dog1.name)
print("Color: ",dog1.color)

dog1.sound()