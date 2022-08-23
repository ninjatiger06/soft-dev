"""
Description: This program asks for a number of grades and then averages them.
Author: Jonas Pfefferman '24
Date: 9/11/20
"""

def main():

    #establishing variables
    numberGrades = int(input("Number of grades: "))
    numberGradesTrue = int(numberGrades + 1)

    #for loop
    totalGrade = 0
    for i in range(1, numberGradesTrue):
        grade = float(input("Grade: "))
        totalGrade = totalGrade + grade

    #calculations
    averageGrade = totalGrade / numberGrades
    print(averageGrade)

main()