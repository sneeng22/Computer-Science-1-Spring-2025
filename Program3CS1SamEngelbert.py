#______________________________________________ 
# Program 3 Computer Science 1 
# Sam Engelbert 
#______________________________________________ 

# asks user for name and greets user 
name = input("What is your name? ")
print(f"Hello there {name}!")
# identify shopping list
shopping_list = []
# menu for choice selection for organizer 
def display_menu(): 
    print("""  
    Shopping List Organizer 
          1. Add an item
          2. Remove an item 
          3. Show all items in list 
          4. Empty whole list 
          5. Calculate total cost of all items 
          6. Exit
          """) 
def add_item(): 
    # strip manages leading whitespace
    name = input("Enter the item name: ").strip()
    quantity = int(input("Enter the quantity of the added item: ")) 
    cost = float(input("Enter the cost per item (in $): $")) 
    # dictionary to help strucutre the given data types
    item = { 
        'name': name, 
        'quantity': quantity, 
        'cost': cost
    } 
    
    shopping_list.append(item) 
# item added message lets user know of successful addition to list 
    print(f"Item '{name}' added!") 
# Decimal Cost Message: F-string for cost of item in consideration of decmal points (true cost)
    print(f"Decimal Cost: ${cost:.2f}") 
# Hexadecimal cost message   
    print(f"Hexadecimal Cost: {hex(int(cost))}") 

def remove_item(): 
    # prompts user to add the item they want to remove
    target = input("Enter the name of the item you need removed: ").strip() 
    found = False 
    for item in shopping_list: 
        if item['name'].lower() == target.lower(): 
            shopping_list.remove(item) 
            print(f"Item '{target}' removed! ") 
            found = True 
            break # breaks for loop 
    if not found: 
        # prompts user to try again if the item is not found in the list
        print(f"Item '{target}' not found in the list.") 

def view_items(): 
    if not shopping_list: 
        print("This shopping list is currently empty!") 
    else: 
        print("\nCurrent Shopping List: ") 
        for idx, item in enumerate(shopping_list, start = 1): 
        # formats entire list to be printed with header, numerical list of item, and cost per item
            print(f"{idx}, {item['name']} - Quantity: {item['quantity']}, Cost per item: ${item['cost']:.2f}")
        
def clear_list(): 
    confirm = input("Are you sure you want to clear your whole list? (Yes/No)").strip().lower() 
    if confirm == 'yes': 
        shopping_list.clear() 
        print("All items have been cleared from your list!") 
    else: 
        print("Operation cancelled!") 

def show_total_cost(): 
    total = sum(item['quantity'] * item['cost'] for item in shopping_list) 
    print(f"Total cost of all items is: ${total:.2f}") 

# while True starts an infinite loop (main program loop) 
    while True: 
        display_menu()
        choice = input("Choose an option (1-6): ").strip() 

        if choice == "1": 
            add_item() 

        elif choice == "2": 
            remove_item() 

        elif choice == "3": 
            view_items() 

        elif choice == "4": 
            clear_list() 

        elif choice == "5": 
            show_total_cost() 

        elif choice == "6":
            print("Thanks for using the 'ole Shopping List Organizer! Good day!")
            break # breaks main loop 
        else: 
            print("Invalid choice type, please try again!")