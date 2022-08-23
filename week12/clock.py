from counter import *

class Clock(object):
    """ a 24-hour clock object, made of three counter objects: one for the seconds
        (0->59), one for the minutes (0->59), and one for the hour (0->23).  """

    def __init__(self, hour, min, sec):
        """ construct counter obj, given hours minutes and seconds """
        self.hour = Counter(24)
        self.hour.setValue(hour)

        self.minutes = Counter(60)
        self.minutes.setValue(min)

        self.seconds = Counter(60)
        self.seconds.setValue(sec)

        self.alarm = [-1, -1, -1]


    def __str__(self):
        """ print info for the object """
        s = "Clock: %02d:%02d:%02d" % (self.getHour(), self.getMinutes(), self.getSeconds())
        return s

    def getTime(self):
        """ getter and formatter for the time """
        s = "%02d:%02d:%02d" % (self.getHour(), self.getMinutes(), self.getSeconds())
        return s

    def setHour(self, h):
        """ setter for hours """
        self.hour.setValue(h)

    def setMinutes(self, m):
        """ setter for minutes """
        self.minutes.setValue(m)

    def setSeconds(self, s):
        """ setter for seconds """
        self.seconds.setValue(s)

    def getHour(self):
        """ getter for hours """
        return self.hour.getValue()

    def getMinutes(self):
        """ getter for minutes """
        return self.minutes.getValue()

    def getSeconds(self):
        """ getter for seconds """
        return self.seconds.getValue()

    def tick(self):
        self.seconds.increment()
        if self.getSeconds() == 0:
            self.minutes.increment()
        if self.getMinutes() == 0 and self.getSeconds() == 0:
            self.hour.increment()

    def setAlarm(self, hours, mins, secs):
        if secs > 59:
            mins += 1
            secs = secs - 60
        if mins > 59:
            hours += 1
            mins = mins - 60
        if hours > 23:
            hours = hours - 24
        self.alarm = "%02d:%02d:%02d" % (hours, mins, secs)

    def getAlarm(self):
        return self.alarm

    def inAlarm(self):
        if self.getTime() == self.alarm:
            return True
        else:
            return False



if __name__ == "__main__":
    c1 = Clock(12,55,21)
    print(c1)
    print("Setting time to 23:59:55...")
    c1.setHour(23)
    c1.setMinutes(59)
    c1.setSeconds(55)
    currentHour = str(c1.getHour())
    print("Hour for c1: %s" % (currentHour))
    print(c1)
    for i in range(15):
        c1.tick()
        print(c1)
