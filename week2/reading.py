"""
    Description: This program helps a student reach a reading deadline
    Author: Jonas Pfefferman '24
    Date: 9/23/20
"""

def main():

    # Getting info from user: total pages, total days
    totalPages = int(input("Pages to read? "))
    pagesLeft = totalPages
    daysLeft = int(input("Days left? "))

    pagesReadTotal = 0
    for i in range(1, daysLeft + 1):
        pagesRead = int(input("\nPages read: "))

        # Pages left, days left, and pages read
        daysLeft += - 1
        pagesReadTotal += pagesRead
        pagesLeft = totalPages - pagesReadTotal

        # Displaying the days and pages left for the user
        print("You have read %i out of %d pages." % (pagesReadTotal, totalPages))
        print("%i pages left, %d days to go." % (pagesLeft, daysLeft))



main()
