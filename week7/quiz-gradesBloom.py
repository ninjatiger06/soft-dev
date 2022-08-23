"""
    Description: This program calculates the average quiz grade for multiple students.
    Author: Mr. Bloom
    Date: Fall 2019
"""

def main():
    # store names and grades in python lists, in case we need them later
    studentNames = []
    studentGrades = []
    studentAverages = []

    # read all names and grades into a list
    gradesFile = open("quiz-grades.txt", 'r')
    for line in gradesFile:
        nameAndGrades = line.split(",")
        name = nameAndGrades[0]
        gradesList = nameAndGrades[1:]
        studentNames.append(name)
        studentGrades.append(gradesList)
    gradesFile.close()

    # find each student's average quiz grade (loop over list of lists)
    studentAverages = []
    for grades in studentGrades:          # for each person
        total = 0
        for grade in grades:                # for each grade in their list of grades
            total += float(grade)
        ave = total / len(grades)
        studentAverages.append(ave)

    # print out each student's name and average quiz grade
    for i in range(len(studentNames)):
        print("%8s: %.1f" % (studentNames[i], studentAverages[i]))


main()
