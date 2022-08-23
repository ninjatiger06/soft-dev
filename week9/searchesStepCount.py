from math import *

def linearSearch(x, L):
    """ return True if x is in L, False if not """

    linearSteps = 0

    for item in L:
        linearSteps += 1
        if item == x:
            return True, linearSteps
    # only gets here if not found!
    return False, linearSteps


def binarySearch(x, L):
    """ return True if x is in L, False if not """

    binarySteps = 0

    # set a low, middle, and high index
    low = 0
    high = len(L) - 1

    #infinite loop for while the lowest value and highest value are not equal
    while low <= high:
        # index the list at the midpoint and compare that item to the one you're searching for
        mid = int((low + high)/2)
        binarySteps += 1

        listItem = L[int(mid)]
        binarySteps += 1
        if listItem == x:
            binarySteps += 1
            return True, binarySteps         # if item is found, exit function and return True

        # if item is not found, see if item is lower/higher (less/greater than) the item at the midpoint
        elif x > listItem:
            low = mid + 1
            binarySteps += 2

        elif x < listItem:
            high = mid - 1
            binarySteps += 2

    return False, binarySteps


if __name__ == "__main__":
    # put test code here
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 5
    print("%3d  %s  %s" % (x, str(L), linearSearch(x, L)))
    assert linearSearch(x, L) == True
    x = 500
    print("%3d  %s  %s" % (x, str(L), linearSearch(x, L)))
    assert linearSearch(x, L) == False

    x = 5
    print("%3d  %s  %s" % (x, str(L), binarySearch(x, L)))
    assert linearSearch(x, L) == True
    x = 500
    print("%3d  %s  %s" % (x, str(L), binarySearch(x, L)))
    assert linearSearch(x, L) == False
