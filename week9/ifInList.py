def linearSearch(lst, element):
    for item in lst:
        if item == element:
            return True
    return False

def linearSearchIndex(lst, element):
    for i in range(len(lst)):
        if element == lst[i]:
            return i
    return -1

def main():

    x = 16
    L = [5,60,34,89,16,33]

    IS_IN_LIST = linearSearch(L, x)
    print(IS_IN_LIST)

    itemIndex = linearSearchIndex(L, x)
    print("Item is located in list  %s at index %d" % (L, itemIndex))



main()
