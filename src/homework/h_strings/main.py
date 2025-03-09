#
import strings

def main():

    user_option = '0'

    while(user_option != '3'):

        print("***DNA***")
        print("1- Hamming Distance")
        print("2- DNA Complement")
        print("3- Exit")

        user_option = input("Make a selection: ")

        if (user_option == '1'):
            
            dna_string = input("Enter a DNA string: ").upper()

            while not strings.valid_dna(dna_string):
                print("Invalid nucleotides used.")
                dna_string = input("Enter a DNA string: ").upper()

            print(f"The length of your string is {len(dna_string)}.")

            dna_string2 = input("Enter a second DNA string that is the same length as the first: ").upper()

            while not strings.valid_dna(dna_string2):
                print("Invalid nucleotides used.")
                dna_string2 = input("Enter a DNA string: ").upper()
            
            while(len(dna_string2) != len(dna_string)):
                dna_string2 = input("Enter a second DNA string that is the same length as the first: ").upper()

            dna_hamming_distance = strings.get_hamming_distance(dna_string, dna_string2)

            print(f"The hamming distance of '{dna_string}' and '{dna_string2}' is {dna_hamming_distance}")

            end_run = '0'
            
            while (end_run != 'y'):
                
                end_run = input("Do you want to exit: Y or N? ")
                    
                if (end_run.upper() == 'Y'):
                    print("Exiting....")
                    break
                    
                elif (end_run.upper() == 'N'):
                    print("Continuing....")
                    break
                else:
                    print("Invalid response. Do you want to exit: Y or N?")

            if (end_run.upper() == 'Y'):
                break
            else:
                continue

        elif (user_option == '2'):

            dna_string = input("Enter a DNA string: ").upper()

            while not strings.valid_dna(dna_string):
                print("Invalid nucleotides used.")
                dna_string = input("Enter a DNA string: ").upper()

            dna_reverse_comp = strings.get_dna_complement(dna_string).upper()

            print(f"The reversed complement to your DNA string '{dna_string}' is '{dna_reverse_comp}'.") 

            end_run = '0'
            
            while (end_run != 'y'):
                
                end_run = input("Do you want to exit: Y or N? ")
                    
                if (end_run.upper() == 'Y'):
                    print("Exiting....")
                    break
                    
                elif (end_run.upper() == 'N'):
                    print("Continuing....")
                    break
                else:
                    print("Invalid response. Do you want to exit: Y or N?")

            if (end_run.upper() == 'Y'):
                break
            else:
                continue

        elif (user_option == '3'):
            
            end_run = '0'
            
            while (end_run != 'y'):
                
                end_run = input("Do you want to exit: Y or N? ")
                    
                if (end_run.upper() == 'Y'):
                    print("Exiting....")
                    break
                    
                elif (end_run.upper() == 'N'):
                    print("Continuing....")
                    break
                else:
                    print("Invalid response. Do you want to exit: Y or N?")

            if (end_run.upper() == 'Y'):
                break
            else:
                user_option = '0'
                continue

        else:
            print("Invalid menu option")

main()