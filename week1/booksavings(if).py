#This program will take your savings and calculate how many of an item you can get with them
#Author: Jonas Pfefferman '24
#Date: 9/2/20

def main ():

    #gathering variables
    textbookSavings = float(input("Enter textbooks savings: "))
    purchaseItem = str(input("What would you like to purchase instead of a book? "))
    purchaseItemCost = float(input("Enter item cost: "))

    #calculating
    numberItems = int(textbookSavings / purchaseItemCost)

    #printing results
    if purchaseItem == ("a child"):
            print("I'M CALLING THE POLICE!")

    else:
        print("You could buy", numberItems, purchaseItem + "(s) with your textbook savings.")

main()
