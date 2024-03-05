# Variables to store data we will use 4 convertation purposes
FAHRENHEIT_MULTIPLIER = 9/5
FAHRENHEIT_CONVERTER = 32
KELVIN_CONVERTER = 273.15

input_temperature_celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit_temperature = input_temperature_celsius * FAHRENHEIT_MULTIPLIER + FAHRENHEIT_CONVERTER
kelvin_temperature = input_temperature_celsius + KELVIN_CONVERTER

print(f"Temperature in Fahrenheit: {fahrenheit_temperature:.2f}F°")
print(f"Temperature in Kelvin: {kelvin_temperature:.2f}K°")