def perform_calculation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Division by zero is not allowed.")
    else:
        raise ValueError("Invalid operator.")


def main():
    while True:
        try:
            num1_input = input("Enter the first number (or 'exit' to quit): ")
            if num1_input.lower() == 'exit':
                print("Exiting the calculator.")
                break

            num1 = float(num1_input)

            num2_input = input("Enter the second number: ")
            num2 = float(num2_input)

            operator = input("Enter an operator (+, -, *, /): ")

            result = perform_calculation(num1, num2, operator)
            print(f"Result is: {result}")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")

        else:
            print("Operation successful.")

        finally:
            print("Hope everything is alright!")


if __name__ == "__main__":
    main()
