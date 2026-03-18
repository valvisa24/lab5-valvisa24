from utils import *

while True:
    op = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit): ").lower().strip()

    if op == "exit":
        break
    
    if op not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]:
        print("Invalid option!")
        continue

    if op == "absolute":
        n = float(input("Enter the number: "))
        result = absolute(n)
    else:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        
        if op == "add": result = add(n1, n2)
        elif op == "subtract": result = sub(n1, n2)
        elif op == "multiply": result = multiply(n1, n2)
        elif op == "divide": result = divide(n1, n2)
        elif op == "exponent": result = exponent(n1, n2)
        elif op == "modulo": result = modulo(n1, n2)
        elif op == "floor_divide": result = floor_divide(n1, n2)

    if isinstance(result, str):
        print(result)
    else:
        print(f"The result is: {result}")
