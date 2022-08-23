class Pizza(object):
    """ class for a single pizza object """

    def __init__(self, toppings):
        """ constructor for pizza class, with the type of pizza """
        self.toppings = toppings
        self.slices = 8

    def __str__(self):
        """ print info for the object """
        s = "%s pizza :: slices left = %d" % (self.toppings, self.slices)
        return s

    def getTopping(self):
        """ getter for the toppings on the pizza """
        return self.toppings

    def getSlices(self):
        """ getter for thee number of slices """
        return self.slices

    def eatSlice(self):
        """ eats a slice of the pizza """
        if self.slices == 0:
            print("No slices left... :(")
            return 0
        else:
            self.slices -= 1


if __name__ == "__main__":
    p1 = Pizza("cheese")
    p2 = Pizza("mushroom and onion")
    print(p1)
    print(p2)

    print("-" * 20)
    print("Num slices left in p2: %s" % p2.getSlices())
    print("Eating a slice of %s!" % p2.getTopping())
    p2.eatSlice()
    print(p2)

    print("-" * 20)
    for i in range(10):
        print("Eating a slice of %s!" % p1.getTopping())
        p1.eatSlice()
        print(p1)
