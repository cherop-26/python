# +-*/, simple calculator,any value
#enter number *2 ,Result
#notify if the operator is invalid


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!"
    else:
        return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def calculator():
    print("Select operator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

operator= input("Enter operator (1/2/3/4): ")

if operator == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
elif operator == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operator == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operator == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
        print("Invalid input!")


calculator()

