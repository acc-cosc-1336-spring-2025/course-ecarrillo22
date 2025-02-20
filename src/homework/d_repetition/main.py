#
import repetition

def main():

    user_option = '0'
    
    while (user_option != '3'):

        print("*******************")
        print("Homework 3 Menu:")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        print("*******************")
        
        user_option = input("Make a selection: ")

        if (user_option == '1'):

            num = int(input("Enter a number between 1 and 10: "))
            
            while (num <= 0 or num >= 10):
                num = int(input("Enter a number between 1 and 10: "))
            
            result = repetition.get_factorial(num)
            
            print(f"The factorial of {num} is {result}")
            print("----------------------------------")
            
            end_run = input("Do you want to exit: Y or N? ")
            
            if (end_run == 'y' or end_run == 'Y'):
                print("Exiting....")
                break
            
            else:
                continue

        elif (user_option == '2'):
            num = int(input("Enter a number between 1 and 100: "))

            while (num <= 0 or num >= 100):
                num = int(input("Enter a number between 1 and 100: "))

            result = repetition.sum_odd_numbers(int(num))
            print(f"The sum of the odd numbers up to {num} is {result}")
            print("----------------------------------")

            end_run = input("Do you want to exit: Y or N? ")
            
            if (end_run == 'y' or end_run == 'Y'):
                print("Exiting....")
                break
            
            else:
                continue

        elif (user_option == '3'):
            
            end_run = input("Do you want to exit: Y or N? ")
            
            if (end_run == 'y' or end_run == 'Y'):
                print("Exiting....")
                break
            
            else:
                continue

        else:
            print("*******************")
            print("Invalid menu option")
            
main()