from graphics import *
from clock import *
from time import sleep
from os.path import isfile

def main():
    if isfile("alarmSettings.txt") == True:
        alarmFile = open("alarmSettings.txt", 'r')
        timeData = alarmFile.readline()

        hours = int(timeData[0:2])
        minutes = int(timeData[3:5])
        seconds = int(timeData[6:8])

        alarmH = int(timeData[11:13])
        alarmM = int(timeData[14:16])
        alarmS = int(timeData[17:19])

    else:
        print("No alarm has been set. Please enter a time and alarm. \nTime:")
        hours = int(input("Hour: "))
        minutes = int(input("Minute: "))
        seconds = int(input("Second: "))
        print("\nAlarm:")
        alarmH = int(input("Hour: "))
        alarmM = int(input("Minute: "))
        alarmS = int(input("Second: "))

    digClock = Clock(hours, minutes, seconds)
    digClock.setAlarm(alarmH, alarmM, alarmS)

    width = 300
    height = 100
    gw = GraphWin("digital clock", width, height)
    gw.setBackground("black")

    ALARM = False
    while True:
        # get current time and display clock
        time = digClock.getTime()
        clockText = Text(Point(width/2, height/2), time)
        clockText.setSize(36)

        if digClock.inAlarm() or ALARM == True:
            gw.setBackground("red")
            clockText.setOutline("yellow")
            ALARM = True
        else:
            gw.setBackground("black")
            clockText.setOutline("green")

        clockText.draw(gw)

        sleep(0.97)        # sleep for 1 second and tick the clock forward one sec
        digClock.tick()

        clockText.undraw()  # undraw old time, so can display the new time

        if gw.checkMouse():
            if ALARM == True:
                ALARM = False
            else:
                break

    gw.close()

    alarmFile = open("alarmSettings.txt", 'w')
    alarmFile.write(str(digClock.getTime()) + " | ")
    alarmFile.write(str(digClock.getAlarm()) + "\n")
    alarmFile.close()

main()
