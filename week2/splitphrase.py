"""Description: this program takes a string and prints half normally and the
                other half going down the page
    Author: Jonas Pfefferman '24
    Date: 9/17/20
"""

def main():

    #Getting the string variable
    strvar = str(input("Enter a string: "))

    #Getting and printing halfway
    halfway = len(strvar) //2
    print(strvar[0:halfway])

    space = halfway * " "

    for char in strvar[halfway:]:
        print("%s%s" % (space,char))

main()
