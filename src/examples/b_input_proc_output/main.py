import input_process_output

def main():
    num1 = input("Enter a number: ") #Python treats input as a string(sequence of characters)
    num2 = input("Enter a number: ")

    result = input_process_output.add_numbers(float(num1), float(num2)) #convert num1, num2 to int
    print(result)

main() #runs the code on line 3
