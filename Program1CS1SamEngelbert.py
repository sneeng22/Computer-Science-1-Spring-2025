#_____________________________________________________
# Program 1: Computer Science 1
# Sam Engelbert 03/05/2025
#_____________________________________________________
def celsius_to_farenheit(celsius): # celsius to fareheit conversion
    return(celsius * 9/5) + 32
 
def meters_to_feet(meters): # meters to feet conversion
    return meters * 3.28084  # to the most reasonable amount of decimal points found on a graphing calculator

def kilograms_to_pounds(kilograms): # kilograms to pounds conversion
    return kilograms * 2.20462 # to the most reasonable amount of decimal points found on a graphing calculator

def decimal_to_binary(decimal): # decimal to binary number conversion
    return bin(decimal)[2:]
def binary_to_decimal(binary): # binary to decimal number conversion
    return int(binary, 2)
# user input seciton name and welcome message
def unit_converter():
    name = input("What is your name? ")
    print(f"Hello there {name}, welcome to the Unit Converter!")
 # generation of selection menu
while True: # selection menu AND while True starts infinte loop until cancelled by a line break 
    print (""" 
1. Celsius-Farenheit
2. Meters-Feet
3. Kilograms-Pounds
4. Decimal-Binary/Binary-Decimal 
5. Quit
""") 
    
    choice = (input("Enter a selection number: ")) # defines choice throughout program

    if choice == "1": # selection "1" from menu selection "celsius to farenheit"
        try:
            c = float(input("Please enter a number in Celsius: "))
            f = celsius_to_farenheit(c) 
            print(f"{c}°C is {f}°F.") # degree conversion
        except ValueError: # invalid input message 
            print("Invlaid input. Please enter a numeric value: ")

    elif choice == "2": # selection "2" from menu selection "meters to feet"
        try: 
            m = float(input("Enter a length value in meters: "))
            ft = meters_to_feet(m)
            print(f"{m} meters is {ft} feet.")
        except ValueError: # invalid input message 
            print("Invalid Input type. Please enter a numeric value: ")
    
    elif choice == "3": # selection "3" from menu selection "kilograms to pounds"
        try: 
            kg = float(input("Enter a weight value in kilograms: "))
            lbs = kilograms_to_pounds(kg) 
            print(f"{kg} kg is {lbs} lbs") 
        except ValueError: # invalid input message   
            print("Invalid Inpiut Type. Please enter a numeric value: ")

    elif choice == "4": # selection "4" from menu selection "decimal to binary" AND "binary to decimal"
        print("1. Decimal-Binary")  
        print("2. Binary-Decimal")
    sub_choice = input("Choose conversion type (Choice 1 or 2): ")
    if sub_choice == "1": # sub_choice to specify which conversion the user wants   
        try: # decimal to binary
            dec = int(input("Enter a decimal number to be converted to binary: ")) 
            binary = decimal_to_binary(dec)
            print(f" The binary representation of {dec} is {binary}.") 
        except ValueError: # invalid input message 
            print("Invalid Input Type. Please enter an integer to be converted: ") 
    elif sub_choice == "2": 
        try: # binary to decimal
            binary_input = input("Enter a binary number to be converted to a decimal number: ") 
            decimal = binary_to_decimal(binary_input) 
            print(f"The decimal representation of {binary_input} is {decimal}.") 
        except ValueError: # invalid input message
            print("Invalid Binary Number.")
        else: # try again from invalid input message 
            print("Invlaid Input Type. Please try again!") 
    
    
    elif choice == "5": # selection "5" from menu selection "quit"
            print("Thank you for using the Unit Converter! Goodbye!") 
            break # ends while True loop

    else: # invalid choice message 
        print("Invalid choice. Please select a valid selection and try again! (1-5): ")

    