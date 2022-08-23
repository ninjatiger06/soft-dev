"""
    Description: This program counts to 100, but if a number is evenly divisible
                 by 3, it says bizz instead of the number. If the number is
                 evenly divisble by 5, it says buzz, and if the number is
                 evenly divisible by 3 and 5, it says bizzbuzz.
    Author: Jonas '24
    Date: 10/5/20
"""

def main():

    for i in range(101):
        if i%3 == 0:
            print("bizz")

        elif i%5 == 0:
            print("buzz")

        elif i%3 == 0 and i%5 == 0:
            print("bizzbuzz")
            
        else:
            print(i)



main()
