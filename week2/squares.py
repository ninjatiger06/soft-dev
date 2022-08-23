#This program will calculate all the squares up to a certain number
#Author: Jonas Pfefferman '24
#Date: 9/9/20

def main():

    #establishing variables
    endNumber = int(input("End number: "))
    endNumberTrue = endNumber + 1

    #calculations and printing
    for i in range(1, endNumberTrue):
        print(i, "x", i, "=", i * i)


main()
