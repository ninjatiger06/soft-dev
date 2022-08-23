"""
	Description: This program helps users keep track of miles run, and lets them
    know whether they met their goal at the end of the running program.
	Author: Mr. Bloom, Jonas Pfefferman
	Date: 11/16/20  (Week 5, Day 2)
"""

#------------------------------------------------------------------------------#
import time

#------------------------------------------------------------------------------#
def getNumbers(days):
	"""
	Purpose: Obtain the miles run per day for all scheduled days
	Parameters: number of days the user will run (int)
	Return Val: a list of numbers of how many miles run per day (list of floats)

	"""
	print("\nHow many miles did you run each day?")

	milesRunList = []
	for day in range(1, days + 1):
		milesRun = float(input("Day %i: " % (day)))
		milesRunList.append(milesRun)
	return milesRunList


#------------------------------------------------------------------------------#
def sumList(distancesList):
	totalDistance = 0
	for distance in distancesList:
		totalDistance += distance
	return totalDistance


#------------------------------------------------------------------------------#
def main():
	# 1. ask the user for a goal (miles run) and number of days to reach goal
	goal = int(input("\nHow many miles do you plan to run? "))
	days = int(input("How many days will it take you to reach your goal? "))

	# 2. getNumbers() obtains the miles run per day and RETURNS a list of numbers.
	# Before you being coding, you need to decide IF we need to send data to
	# getNumbers() for it to do its job.  In other words, what data/info/nowledge
	# does getNumbers() need to complete the task outlined above?  IF we do
	# need to send data, then what data (variables) are we sending, and how many?
	# The variables you decide on will be the inputs (arguments/parameters) to
	# your getNumbers() function.
	distancesList = getNumbers(days)

	# 3. sumList() calculates the total progress made (number of miles ran).
	progress = sumList(distancesList)
	print("You ran %i miles in %i days." % (progress, days))

    # 4. output whether user met, exceeded, or fell short of their goal
	if progress > goal:
		print("You exceeded your goal!")
	elif progress == goal:
		print("You met your goal!")
	else:
		print("You did not meet your goal.")



main()
#------------------------------------------------------------------------------#
