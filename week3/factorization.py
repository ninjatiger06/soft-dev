"""
    Description: This program finds all the factors of a given integer
    Author: Jonas Pfefferman '24
    Date: 10/13/20
"""

import math

def main():

    # Getting the integer from user input
    product = int(input("Enter a number to factor: "))
    productFactors = 0

    # For loop for every way to multiply the number up to its square root
    for factor1 in range(1, int(math.sqrt(product)) + 1):

        # If statement to only print factors that multiply to the number
        if product % factor1 == 0:
            factor2 = product / factor1
            productFactors += 1
            print("%i x %i = %i" % (factor1, factor2, product))

    if productFactors == 1:
        print("%i is a prime number." % (product))



main()
