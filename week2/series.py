"""
    Description: This program calculates the sum of a geometric series
    Author: Jonas Pfefferman '24
    Date: 9/23/20
"""

def main():

    # Getting the number of terms and denominator ratio from the user
    demRatio = int(input("denominator ratio (k): "))
    numberTerms = int(input("number of terms (n): "))

    # For loop for calculations
    runningTotal = 0
    denominatorCounter = 1
    for i in range(1, numberTerms + 1):
        runningTotal += 1 / denominatorCounter
        denominatorCounter = denominatorCounter * demRatio

    # Displaying Results
    print("sum:", runningTotal)



main()
