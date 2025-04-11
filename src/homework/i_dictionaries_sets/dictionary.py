#
inventory_dict = {}

def add_inventory(inventory_dictionary, widget_name, quantity):
    
    if widget_name not in inventory_dictionary:
        inventory_dictionary[widget_name] = quantity
    
    if widget_name in inventory_dictionary:
        inventory_dictionary[widget_name] = quantity

def remove_inventory(inventory_dictionary, widget_name):

    if widget_name in inventory_dictionary:
        del inventory_dictionary[widget_name]
        print("Record deleted.")
    else:
        print("Item not found.")

def display_menu():

    print("1-Add or Update Item")
    print("2-Delete Item")
    print("3-Exit")

def run_menu():

    menu_option = 0
    exit = ''

    while (menu_option != '0'):
        
        display_menu()
        menu_option = input("Enter menu option: ")

        handle_menu_option(menu_option)

        if (menu_option == '3'):
            exit = input("Do you want to exit? Y or N: ")

        if (exit == 'Y' or exit == 'y'):
            print("Exiting...")
            menu_option = '0'

def handle_menu_option(choice):
        
    if(choice == '1'):

        item = input("Enter an item: ")
        quantity = input("Enter the quantity of that item: ")

        add_inventory(inventory_dict, item, quantity)

        print(f"Here is your updated inventory: {inventory_dict}")

    if(choice == '2'):

        item = input("Enter the item you wish to delete: ")

        remove_inventory(inventory_dict, item)

        print(f"Here is your updated inventory: {inventory_dict}")