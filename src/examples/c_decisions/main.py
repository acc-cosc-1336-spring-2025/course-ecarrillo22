import decisions

def main():
    year = input("Enter year: ")

    result = decisions.get_generation(int(year))

    print (result)

main()
