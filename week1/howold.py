#This program will tell you how old you are
#Author: Jonas Pfefferman '24
#Date: 8/27/20

def main():

    currentYear = int(2020)
    birthYear = int(input("Enter the year you were born: "))

    age = currentYear - birthYear

    print ("At some point this year, you will be", age, "years old.")

main()
