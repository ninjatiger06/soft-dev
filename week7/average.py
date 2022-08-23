"""
    Description: This program reads in values from grades.txt and computes the average.
    Author: Mr. Bloom
    Date: Fall 2019
"""

def main():
    # store grades in python list, in case we need them later
    grades = []

    # read all grades into a list
    gradesFile = open("grades.txt", 'r')
    for line in gradesFile:
        #strip removes extra spacing at the end of a string/line
        grade = float(line.strip())
        grades.append(grade)
    gradesFile.close()

    # find average of grades in list
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    print("ave grade = %.2f" % average)


main()
