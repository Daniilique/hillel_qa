def square(side):
    perimeter = 4 * side
    area = side * side
    diagonal = side * (2**0.5)  # Using math.sqrt is also possible

    print(f"Perimeter of the square: {perimeter}")
    print(f"Area of the square: {area}")
    print(f"Diagonal of the square: {diagonal:.2f}")  # Format diagonal to 2 decimal places

# Just to try out
square(5)