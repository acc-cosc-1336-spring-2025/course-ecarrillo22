#
import decisions

def main():
    #prompts user for options
    options = input ('Enter an option: ')
    total = input ('Enter a total: ')

    #creates a result variable from options ratio function
    result = decisions.get_options_ratio(float(options), float(total))

    #displays the rating 
    print(f'The rating is {decisions.get_faculty_rating(result)}')

main()