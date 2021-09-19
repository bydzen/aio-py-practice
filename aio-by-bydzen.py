#########################################################
# Author        : Sultan Kautsar                        #
# Last Edited   : Sunday September 19, 2021 @ 11:50 AM  #
# Description   : All-in-one pyhton programs            #
#########################################################

# Import os for call system commands
import os

# Clear screen/console on Microsoft Windows
os.system('cls')

print("Choose program:")
print("1. Countdown\n2. Shuffle Deck\n3. Simple Calculator\n4. Calendar")
print("0. Exit")

x = int(input("Enter num: "))

if x == 1:
    import time

    os.system('cls')
    print("*=== Countdown Program ===*\n")

    def countdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec -= 1

        print("stop!")

    countdown(5)

elif x == 2:
    import itertools
    import random

    os.system('cls')
    print("*=== Shuffle Deck Cards Program ===*\n")

    # Make a deck of cards
    deck = list(itertools.product(range(1, 14), [
                'Spade', 'Heart', 'Diamond', 'Club']))

    # Shuffle the cards
    random.shuffle(deck)

    # Draw five cards
    print("You got:")
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])

elif x == 3:
    # Program make a simple calculator
    os.system('cls')
    print("*=== Calculator Program ===*\n")

    # This function adds two numbers
    def add(x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y

    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    print()

elif x == 4:
    # Program to display calendar of the given month and year
    os.system('cls')
    print("*=== Calendar Program ===*\n")

    # Importing calendar module
    import calendar

    # To take month and year input from the user
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))

    # Display the calendar
    print("\n", calendar.month(yy, mm))

elif x == 0:
    print("\nExited.")

else:
    print("\nNo choice, sorry.")

# End of program
