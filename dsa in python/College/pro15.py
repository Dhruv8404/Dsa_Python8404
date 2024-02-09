def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculator():
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        print(f"\n{num1} + {num2} = {add(num1, num2)}")
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Run the calculator
calculator()
