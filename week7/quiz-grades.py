"""
    Description: Looks through a text file with a student's name and their grades
                 and then prints out their names and their grade average
    Date: 1/12/21
    Author: Jonas Pfefferman '24
"""

def main():

    studentNames = []
    studentGrades = []

    gradesFile = open("quiz-grades.txt", 'r')
    for line in gradesFile:
        line = line.strip()
        lineList = line.split(",")
        name = lineList[0]
        studentNames.append(name)
        grades = lineList[1:]
        studentGrades.append(grades)
    gradesFile.close()

    studentAverages = []
    for gradeList in studentGrades:
        sum = 0
        for grade in gradeList:
            sum += grade
        average = float(sum / len(gradeList))
        studentAverages.append(average)

    for i in range(len(studentNames)):
        print("%s: %i" % (studentNames[i], studentAverages[i]))



main()
