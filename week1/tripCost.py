"""
    Description: This program will compute the cost of a multi-day trip for one
                 or more people.
    Author: Jonas Pfefferman '24
    Date: 9/3/20
"""

def main ():

    print("Let's go on a trip!\n")

    # Getting trip info: travel cost, food/lodging cost, days, number of people
    personTravelCost = float(input("What is the travel cost per person? "))
    personFoodCost = float(input("What is the food/lodging cost per person per day? "))
    travelDays = int(input("How many days will you be traveling? "))
    numberPeople = int(input("How many people are going? "))

    # Calculations for single person
    personTotalFoodCost = float(personFoodCost * travelDays)
    personTotalBill = float(personTotalFoodCost + personTravelCost)

    # calculations for total
    totalTravelCost = float(personTravelCost * numberPeople)
    peopleFoodCost = float(personFoodCost * numberPeople)
    totalFoodCost = float(peopleFoodCost * travelDays)
    totalBill = float(totalTravelCost + totalFoodCost)

    # Turning Floats/Integers into Strings
    personTotalBillString = str(personTotalBill)
    totalBillString = str(totalBill)


    # Printing results
    print("Cost per person: ", "$" + personTotalBillString)
    print("Total cost: ", "$" + totalBillString)



main()
