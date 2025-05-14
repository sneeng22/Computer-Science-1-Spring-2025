#________________________________________ 
# Program 4 & 5 Computer Science 1 
# Sam Engelbert 
#________________________________________ 

# prompts user to input name, greeting message 
name = input("What is your name? ") 
print(f"Hello there {name}, welcome to the Timesheet Manager!") 

# main list type defined throught program 
employee_list = []

def display_menu(): 
    print(""" 
        Choose a selection from the menu: 
    1. Add An Employee
    2. Remove An Employee
    3. View All Employees
    4. Calculate Total Payroll
    5. Hours to Other Numeral Unit Conversion
    6. Bitwise Operation
    7. Exit
          """) 
# Prompts user to add new employee and stores data within the list
def add_employee(): 
# New Employee ID (integer)
    emp_id = id = int(input("Enter Employee ID: ")) 
    name = input("Enter New Employee Name: ").strip() 
    hours = float(input("Enter Hourly Rate: ")) 
    rate = float(input("Enter Hourly Rate: ")) 
    employee_list.append([emp_id, name, hours, rate]) 
    print(f"Eployee addedL ID={emp_id}, Name = {name}")  

def remove_employee(): 
    target_id = int(input("Enter Employee ID: ")) 
    for emp in employee_list:  
        if emp[0] == target_id: 
            employee_list.remove(emp) 
            print(f"Employee ID {target_id} removed!") 
            return 
        print("Employee not found!") 

def view_all_employees():  
# Displays all employees on the timesheet list 
    if not employee_list: 
        print("!No Employees found!") 
        return 
    print("\nCurrent Employees: ") 
    for emp in employee_list: 
        print(f"ID: {emp[0]}, Name: {emp[1]}, Hours: {emp[2]}, Rate: ${emp[3]:2f}") 

def calculate_total_payroll(): 
# Takes total payroll of employees and displays them 
    total = sum(emp[2] * emp[3] for emp in employee_list) 
    print(f"The total payroll of all employees is: ${total:.2f}")

def convert_hours_numeral(): 
    target_id = int(input("Enter Employee ID: "))  
    for emp in employee_list:
        if emp [0] == target_id: 
            hours = int(emp[2]) 
            print(f"Employee ID: {target_id}") 
            print(f"Decimal Hours: {hours}")
            print(f"Binary Hours: {bin(hours)}") 
            print(f"Hexadecimal Hours: {hex(hours)}") 
            return 
        print("!Employee not found!") 
def bitwise_demo(): 
    print(""" 
        Choose a Bitwise Operation! 
    1. Shift LEFT
    2. Shift RIGHT
    3. AND
    4. OR
    5. XOR
        """) 
choice = input("Enter choice: ") 

x = int(input("Enter first integer: ")) 
if choice in ['1', '2']: 
    shift = int(input("Enter number of bits needed to shift: ")) 
    if choice == '1': 
        result = x << shift 
        print(f"{x} shifted right by right by {shift} = {result}") 
    else: 
        result = x >> shift 
        print(f"{x} shifted right by {shift} = {result}") 
else: 
    y = int(input("Enter second integer: ")) 
    if choice == '3': 
        print(f"{x} AND {y} = {x & y}") 
    if choice == '4': 
        print(f"{x} OR {y} = {x | y}") 
    if choice == '5': 
        print(f"{x} XOR {y} = {x ^ y}") 
    else: 
        print("Invalid choice, please try again!") 

# program main loop, driven by while True which is an infinite loop until cancellation
def main(): 
    while True: 
        display_menu()
        choice = input("Select option (1-7): ").strip() 
        if choice == '1':  
            add_employee() 
        elif choice == '2': 
            remove_employee() 
        elif choice == '3': 
            view_all_employees() 
        elif choice == '4': 
            calculate_total_payroll() 
        elif choice == '5': 
            convert_hours_numeral() 
        elif choice == '6': 
            bitwise_demo() 
        elif choice == '7': 
            print("Thanks for using the Timesheet Manager! Bye!")  
        else: 
            print("Invalid choice, please try again!") 


    

