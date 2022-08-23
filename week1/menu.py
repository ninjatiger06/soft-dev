#This is a mad-lib type activity that creates a menu blurb
#Author: Jonas Pfefferman '24
#Date: 8/27/20

def main ():

    soup = str(input("Please enter the soup of the day: "))
    special = str(input("Please enter today's special: "))
    dessert = str(input("Please enter today's dessert: "))

    print("Welcome to Python Plaza!")
    print("Our soup of the day is", soup)
    print("Today's special is", special)
    print("And today's dessert is our world-famous", dessert)

main()
