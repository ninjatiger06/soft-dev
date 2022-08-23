"""
    Description: This program prompts the user for a year and then prints
                 whether or not that year is a leap year.
    Author: Jonas Pfefferman '24
    Date: 10/9/20
"""

def main():

    # Getting the year from user-input
    year = int(input("Enter a year: "))

    # If the year is divisible by 100, it also must be divisible by 400 to be
    # a leap year
    if year % 100 == 0:   # Checking if the year is evenly divisible by 100
        if year % 400 == 0:   # Checking if the year is also divisible by 4
            print("%i is a leap year." % (year))

        else:
            print("%i is NOT a leap year." % (year))

    else:
        if year % 4 == 0:    # Checking if the year is divisible by 4
            print("%i is a leap year." % (year))

        else:
            print("%i is NOT a leap year." % (year))



main()
