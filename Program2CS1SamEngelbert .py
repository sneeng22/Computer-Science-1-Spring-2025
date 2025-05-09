#____________________________________________
# Program 2: Computer Science 1 
# Sam Engelbert 
#____________________________________________ 

# user input section, name and greet
name = input("What is your name? ") # Prompts user input 
print(f"Hello there {name}, welcome to the Number-Proccessing Tool!") # Greets user of the program

# Menu Selection function and user input definition  
def display_menu():
   
    print("""print
1. Display all numbers   
2. Display only even numbers 
3. Calculate the sum and average    
4. Perform a bitwise operation
5. Check if the target value is present 
6. Quit 
""")
    # prompts user to enter 4 numbers post menu selection os "1-5"
    input_line = input("Please enter a set of 4 single digit integers, seperate each one with a space: ")
    values = [int(x) for x in input_line.split()]
    assert len(values) == 4, "Enter exactly 4 integers"

    # while True starts infinte program loop 
    while True: 
        display_menu() 
        choice = input("Enter a choice from the menu 1-6")
    
        if choice == "1": 
            print("All numbers are:", *values, sep = " , ")
        
        elif choice == "2":
            print("All even numbers given:", end = " ")
            for val in values:
                if val % 2 == 0: 
                    print(val, end = " ") 
            print() 
        
        elif choice == "3": 
            total = sum(values) 
            average = total / len(values) 
            print(f"Sum {total}, Average: {average:.2f}") 
        
        # Bitwise Caculation: AND, OR, XOR (Exclusive OR)
        elif choice == "4": 
            print("Choose a(n) bitwise operation to perform: AND, OR, XOR") 
            operation = input("Enter preferred operation: ") 

            result = values[0] 
            for val in values[1:]: 
                if operation == "AND": 
                    result &= val 
                elif operation == "OR": 
                    result |= val 
                elif operation == "XOR": 
                    result ^= val 
                else: # invalid input message 
                    print("Invalid input, please try again!") 
            else: 
                print(f"Result of bitwise operation {operation}: {result}") 
        # user input selection "5" target value from four number list    
        elif choice == "5": 
            target = int(input("Enter a target calue (single digit only!): ")) 
            if target in values: 
                print(f"{target} is in the list of numbers you provided!") 
            else: 
                print(f"{target} is not in the list of numbers you provided :( ") 
        # Darn :(
        
        # user input selection "6" amd program loop break (end)
        elif choice == "6": 
            print("Thank you for using the Number-Proccessing Tool!")
            break 
        # invalid input message 
        else: 
            print("Invalid input, please try again!")
