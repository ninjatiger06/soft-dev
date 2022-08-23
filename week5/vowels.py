def capitalizeVowels(myList):
    """count and capitalize the vowels"""
    count = 0
    for i in range(len(myList)):
        if isVowel(myList[i]):
          myList[i] = myList[i].upper()
          count += 1
    return count

def isVowel(ch):
    """return True if ch is a vowel, False if not"""
    vowels = "aeiou"
    if ch.lower() in vowels:
        return True
    else:
        return False

def main():
    S = "we love comp sci!"
    L = list(S)
    numVowels = capitalizeVowels(L)
    newS = "".join(L)
    print(numVowels)
    print(newS)


main()
