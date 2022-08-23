#This program will create a triangle of sorts using a certain character up to a certain number of lines
#Author: Jonas Pfefferman '24
#Date: 9/9/20

def main():

    #establishing variables
    char = str(input("Character: "))
    num = int(input("Number: "))
    numTrue = num + 1

    #loop
    for i in range(1, numTrue):
        print(char * i)

main()
