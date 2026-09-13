class Calculator:
    def addition(self, a,b):
        result = a+b
        return result

    def subtraction(self,a,b):
        result = a-b
        return result

    def multiplication(self,a,b):
        result = a*b
        return result

    def division(self,a,b):
        result = a/b
        return result
    
cal = Calculator()
num1 = int(input(" Enter first number: "))
num2 = int(input(" Enter second number: "))
        

print("===== Cauculator =====")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Divison")
choice = int(input(" Enter opeartion: "))
match choice:
    case 1:
        result = cal.addition(num1,num2)
        print(f"Result: {result}")
    case 2:
        result = cal.subtraction(num1,num2)
        print(f"Result: {result}")
    case 3:
        result = cal.multiplication(num1,num2)
        print(f"Result: {result}")
    case 4:
        result = cal.division(num1,num2)
        print(f"Result: {result}")

        

