def main():

    myAnswers = []
    correctAnswers = []
    correct = 0
    incorrect = 0
    total = 0

    myAnswersFile = open("MyAnswers2.txt", 'r')
    for line in myAnswersFile:
        line = line.strip()
        lineList = line.split("\n")
        myAnswer = lineList[0]
        myAnswers.append(myAnswer)
    myAnswersFile.close()

    correctAnswersFile = open("CorrectAnswers2.txt", 'r')
    for line in correctAnswersFile:
        line = line.strip()
        lineList = line.split("\n")
        correctAnswer = lineList[0]
        correctAnswers.append(correctAnswer)
    correctAnswersFile.close()

    for i in range(len(myAnswers)):
        if myAnswers[i] == correctAnswers[i]:
            correct += 1
            #print("#%i: Correct" % (i+1))
        else:
            incorrect += 1
            print("#%i: Incorrect" % (i+1))
            print("You answered: %s, Correct Answer: %s\n" % (myAnswers[i], correctAnswers[i]))
        total += 1

    print("\n-----------")
    print("Number Correct: %i" % (correct))
    print("Number Incorrect: %i" % (incorrect))
    print("Percentage Correct: %i" % ((correct/total)*100))



main()
