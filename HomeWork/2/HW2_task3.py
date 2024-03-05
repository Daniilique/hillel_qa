while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except:
        print("Invalid input. Please enter numbers only.")
# Operrator check
operator = input("Enter an operator (+, -, *, /): ")
if operator not in ["+", "-", "*", "/"]:
    print("Invalid operator. Please use +, -, *, or /.")
    exit()
# Calculations
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2 if num2 != 0 else "Divided by ZERO is invalid"
print(f"Result is: {result}")
print("Hope everything is allright!")