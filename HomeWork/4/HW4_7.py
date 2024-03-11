attempts = 0

while attempts < 2:
    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")

    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        attempts += 1

if attempts == 2:
    print("End of requests")
    exit()

attempts = 0

while attempts < 2:
    operator = input("Enter an operator (+, -, *, /): ")

    if operator in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        attempts += 1

if attempts == 2:
    print("End of requests")
    exit()

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    if num2 != 0:
        result = num1 / num2
    else:
        print("Division by zero is not allowed.")
        exit()

print(f"Result is: {result}")
print("Hope everything is alright!")
