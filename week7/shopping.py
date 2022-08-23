"""
    Description: Reads and displays information from shoppingList.txt
    Author: Jonas Pfefferman '24
    Date: 1/18/21
"""

def main():

    listFile = open("c:/Users/Jonas/OneDrive/Desktop/School/2020-2021/soft-dev/week7/shoppingList.txt", 'r')
    for line in listFile:
        item = line.strip()
        print(item + "\n")
    listFile.close()



main()
