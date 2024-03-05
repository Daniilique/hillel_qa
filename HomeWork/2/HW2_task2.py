v1 = float(input("Enter ammount of water for V1: "))
t1 = float(input("Enter the temperature of T1: "))
v2 = float(input("Enter amount of water for V2: "))
t2 = float(input("Enter the temperature of T2: "))
#Calculations
amount = v1 + v2
volume = (v1 * t1 + v2 * t2) / amount
#final_calc = volume / amount
print(f"We will calculate the results based on this formula bellow.")
print(f" (v1 * t1 + v2 * t2)/v1 + v2 ")
# Print the results
print(f"The resulting volume of the mixture is: {amount:.2f} liters")
print(f"The resulting temperature of the mixture is: {volume:.2f} °C")