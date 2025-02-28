#
import value_return, void_func

def main():

    void_func.welcome_message()
    epoch_seconds = int(input("Enter an epoch time: "))

    hours = value_return.get_hour(epoch_seconds)
    minutes = value_return.get_minutes(epoch_seconds)
    seconds = value_return.get_seconds(epoch_seconds)

    print(f"The time is {hours:02}:{minutes:02}:{seconds:02}")

main()