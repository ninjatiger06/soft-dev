"""
    Description: Looks through a text file with a student's name and their grades
                 and then prints out the student's name, grades, and average on
                 the same file.
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

    allFieldsFile = open("quiz-grades.txt", 'w')
    for i in range(len(studentAverages)):
        allFieldsFile.write("%s: %s; %i \n" % (studentNames[i], studentGrades[i], studentAverages[i]))
    allFieldsFile.close()



main()
