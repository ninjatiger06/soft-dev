"""
    Description: This program takes the user's weight, age, gender, mile time,
                 and heartrate. It then calculates the Vo2 max and a rating,
                 based on Vo2 max values for 20-29 year olds.
    Author: Jonas Pfefferman '24
    Date: 11/20/20
"""

def main():

    weight = int(input("body weight (lbs): "))
    age = int(input("age (yrs): "))
    gender = str(input("gender (m/f): "))
    time = int(input("mile time (min): "))
    rate = int(input("heart rate (b/m): "))

    vo2MaxPart = float(132.853 - (0.0769 * weight) - (0.3877 * age) - (3.2649 * time) - (0.1565 * rate))

    if gender == "m":
        vo2Max =  float(vo2MaxPart + (6.3150 * 1))
    else:
        vo2Max = float(vo2MaxPart + (6.3150 * 0))

    if gender == "m":
        if vo2Max < 33.0:
            print("VO2max = %.2f .... Very Poor" % (vo2Max))
        elif vo2Max <= 33.0 and vo2Max >= 36.4:
            print("VO2max = %.2f .... Poor" % (vo2Max))
        elif 36.5 <= vo2Max <= 42.4:
            print("VO2max = %.2f .... Fair" % (vo2Max))
        elif vo2Max <= 42.5 and vo2Max >= 46.4:
            print("VO2max = %.2f .... Good" % (vo2Max))
        elif vo2Max <= 46.5 and vo2Max >= 52.4:
            print("VO2max = %.2f .... Excellent" % (vo2Max))
        else:
            print("VO2max = %.2f .... Superior" % (vo2Max))

    else:
        if vo2Max < 23.6:
            print("VO2max = %.2f .... Very Poor" % (vo2Max))
        elif vo2Max <= 23.6 and vo2Max >= 28.9:
            print("VO2max = %.2f .... Poor" % (vo2Max))
        elif vo2Max <= 29.0 and vo2Max >= 32.9:
            print("VO2max = %.2f .... Fair" % (vo2Max))
        elif vo2Max <= 33.0 and vo2Max >= 36.9:
            print("VO2max = %.2f .... Good" % (vo2Max))
        elif vo2Max <= 37.0 and vo2Max >= 41.0:
            print("VO2max = %.2f .... Excellent" % (vo2Max))
        else:
            print("VO2max = %.2f .... Superior" % (vo2Max))



main()
