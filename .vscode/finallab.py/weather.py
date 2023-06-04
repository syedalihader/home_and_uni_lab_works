def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

print("Temperature Conversion Program")

while True:
    print("Please select an option:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Celsius to Kelvin")
    print("3. Convert Fahrenheit to Celsius")
    print("4. Convert Fahrenheit to Kelvin")
    print("5. Convert Kelvin to Celsius")
    print("6. Convert Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Thank you for using the temperature conversion program. Goodbye!")
        break

    temperature = float(input("Enter the temperature: "))

    converted_temperature = None

    if choice == '1':
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temperature}°F")
    elif choice == '2':
        converted_temperature = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equal to {converted_temperature}K")
    elif choice == '3':
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temperature}°C")
    elif choice == '4':
        converted_temperature = fahrenheit_to_kelvin(temperature)
        print(f"{temperature}°F is equal to {converted_temperature}K")
    elif choice == '5':
        converted_temperature = kelvin_to_celsius(temperature)
        print(f"{temperature}K is equal to {converted_temperature}°C")
    elif choice == '6':
        converted_temperature = kelvin_to_fahrenheit(temperature)
        print(f"{temperature}K is equal to {converted_temperature}°F")


