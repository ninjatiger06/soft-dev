"""
    Description: This program reads in student names and values from
    average-grades.txt and computes the class' average grade.
    Author: Mr. Bloom
    Date: Fall 2019
"""

def main():
    # store average grades in python list, in case we need them later
    grades = []

    # read all grades (averages) into a list
    gradesFile = open("class-grades.txt", 'r')
    for line in gradesFile:
        lineList = line.split(",")      # split string on comma and save into list
        average = float(lineList[1])    # get avg, 2nd item in list, & convert to float
        grades.append(average)
    gradesFile.close()

    # find class average by adding up students' grades and dividing by num students
    total = 0
    for avg in grades:
        total += avg
    classAverage = total / len(grades)
    print("ave grade = %.1f" % classAverage)


main()
