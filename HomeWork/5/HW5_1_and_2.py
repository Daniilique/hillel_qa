def calculate_square_root():
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        result = num ** 0.5
        print(f"The square root of {num} is: {result}")
    except ValueError as e:
        print(e)
    finally:
        print("Calculation operation completed.")
calculate_square_root()
