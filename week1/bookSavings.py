"""
    Description: This program will take your savings and calculate how many of
                 an item you can get with them
    Author: Jonas Pfefferman '24
    Date: 9/2/20
"""

def main ():

    # Getting info from user: savings, item, and cost of item
    textbookSavings = float(input("Enter textbooks savings: "))
    purchaseItem = str(input("What would you like to purchase instead of a book? "))
    purchaseItemCost = float(input("Enter item cost: "))

    # Calculating
    numberItems = int(textbookSavings / purchaseItemCost)

    # Printing results
    print("You could buy %s %s(s) with your textbook savings." % (numberItems, purchaseItem))



main()
