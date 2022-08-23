class Counter(object):
    """ an object that keeps track of some value, where the value starts at zero,
    counts up to some maximum value, and then resets back to zero. """

    def __init__(self, max):
        """ constructor for counter class, with the maximum number """
        self.max = max
        self.value = 0

    def __str__(self):
        """ print info for the object """
        s = "Value: %d    (MaxValue = %d)" % (self.value, self.max)
        return s

    def getValue(self):
        return self.value

    def getMaxValue(self):
        return self.max

    def increment(self):
        self.value += 1
        if self.value == self.max:
            self.value = 0

    def setValue(self, newValue):
        if newValue > self.max - 1:
            self.value = newValue - (self.max - 1)
        else:
            self.value = newValue



if __name__ == "__main__":                      # test code
    c = Counter(60)    # create 0 -> 59 counter object
    print(c)
    for i in range(10):
        c.increment()    # test increment() method
        print(c)

    print("-"*20)
    print("set counter value to 55")

    c.setValue(55)
    print(c)
    for i in range(10):
        c.increment()    # test roll-over of counter
        print(c)
