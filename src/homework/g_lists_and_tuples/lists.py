#
def get_lowest_list_value(num_list):

    lowest_num = num_list[0]
    
    for num in num_list:
        if num < lowest_num:
            lowest_num = num
    
    return lowest_num

def get_highest_list_value(num_list):

    highest_num = num_list[0]

    for num in num_list:
        if num > highest_num:
            highest_num = num

    return highest_num

def display_menu():
    
    print("1-Show list's highest and lowest values")
    print("2-Exit")

def run_menu():
    
    menu_option = 0
    exit = ''

    while (menu_option != '0'):
        
        display_menu()
        menu_option = input("Enter menu option: ")

        handle_menu_option(menu_option)

        if (menu_option == '2'):
            exit = input("Do you want to exit? Y or N: ")

        if (exit == 'Y' or exit == 'y'):
            print("Exiting...")
            menu_option = '0'

def handle_menu_option(option):
        
    if (option == '1'):

        num_list = []
        add_more = 'y'

        while (len(num_list) <= 2):
            num = int(input("Enter a value for your list: "))
            num_list.append(num)

        while (add_more == 'y'):
            add_more = input("Do you want to enter another value? Y or N: ")
            
            if (add_more.lower() == 'y'):
                num = int(input("Enter another value for your list: "))
                num_list.append(num)

        lowest_value = get_lowest_list_value(num_list)
        highest_value = get_highest_list_value(num_list)

        print(f"Your list is {num_list}.")
        print(f"The lowest value in your list is {lowest_value}.")
        print(f"The highest value in your list is {highest_value}.")

