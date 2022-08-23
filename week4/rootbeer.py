"""
    Description: This program 'sings' the '99 Bottles of Rootbeer on the Wall' song.
    Author: Mr. Bloom/Jonas Pfefferman '24
    Date: 10/20/20
"""

def bottles(n):
    """ print song lyrics for n bottles """
    print("%i bottle of rootbeer on the wall," % (n))
    print("%i bottle of rootbeer," % (n))
    print("Take one down and pass it around,")
    print("%i bottles of rootbeer on the wall.\n" % (n-1))

def main():

    for i in range(100, 0, -1):
        bottles(i)



main()
