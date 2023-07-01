def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Prompt the user for the conversion type and input temperature
conversion_type = input("Enter the conversion type (C to F or F to C): ").upper()
temperature = float(input("Enter the temperature to convert: "))

if conversion_type == "C TO F":
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {converted_temperature}°F")

elif conversion_type == "F TO C":
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F = {converted_temperature}°C")

else:
    print("Invalid conversion type. Please enter 'C to F' or 'F to C'.")
