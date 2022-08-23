"""
    Description: Looks through a text file with a student's name and their grades
                 and then creates a new file where their names and averages are
                 stored.
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
            sum += int(grade)
        average = sum / len(gradeList)
        studentAverages.append(average)

    averagesFile = open("quiz-averages.txt", 'w')
    for i in range(len(studentAverages)):
        averagesFile.write("%s,%i \n" % (studentNames[i], studentAverages[i]))
    averagesFile.close()



main()
