# Temperature converter
select = input("Choose one option: \n For C to F press 1: \n For F to C press 2: \n For F to K press 3: \n For K to F press 4: \n For K to C press 5: \n For C to K press 6: ")

if select == "1":
    print("Celsius to Fahrenheit Conversion")
    temp = float(input("Enter the temperature in Celsius: "))
    temp = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {temp} °F")
    
elif select == "2":
    print("Fahrenheit to Celsius Conversion")
    temp = float(input("Enter the temperature in Fahrenheit: "))
    temp = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {temp} °C")
    
elif select == "3":
    print("Fahrenheit to Kelvin Conversion")
    temp = float(input("Enter the temperature in Fahrenheit: "))
    temp = (temp - 32) * 5/9 + 273.15
    print(f"The temperature in Kelvin is: {temp} K")
     
elif select == "4":
    print("Kelvin to Fahrenheit Conversion")
    temp = float(input("Enter the temperature in Kelvin: "))
    temp = (temp - 273.15) * 9/5 + 32
    print(f"The temperature in Fahrenheit is: {temp} °F")

elif select == "5":
    print("Kelvin to Celsius Conversion")
    temp = float(input("Enter the temperature in Kelvin: "))
    temp = temp - 273.15
    print(f"The temperature in Celsius is: {temp} °C")
    
elif select == "6":
    print("Celsius to Kelvin Conversion")
    temp = float(input("Enter the temperature in Celsius: "))
    temp = temp + 273.15
    print(f"The temperature in Kelvin is: {temp} K")
else:
    print("Invalid Input")
