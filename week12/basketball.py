class NBAPlayer(object):
    """ class for single NBA player object """

    def __init__(self, name, number, team):
        """ constructor for player object, given name, etc """

        # any self.whatever variable is DATA for this object,
        # and can be used in any methods in this class

        self.name = name
        self.number = int(number)       # jersey number
        self.team = team
        self.gp = 0                     # games played
        self.pts = 0                    # points scored
        self.rbds = 0                   #rebounds caught

    def __str__(self):
        """ pretty-print info about this object """
        s = "%15s #%d -- Team: %20s" % (self.name, self.number, self.team)
        s += "\n\t\tGP: %3d, PTS: %3d, RBDS: %3d" % (self.gp, self.pts, self.rbds)
        return s

    def playGame(self, points, rebounds):
        """ example of adding data to player object """
        self.gp += 1
        self.pts += points
        self.rbds += rebounds

    def ppg(self):
        """ calculate average points per game """
        if self.gp == 0:
            return 0
        else:
            avg = self.pts / self.gp
            return avg

    def rpg(self):
        """ calculate average rebounds per game """
        if self.gp == 0:
            return 0
        else:
            avg = self.rbds / self.gp
            return avg

    def getName(self):
        """ getter for player name """
        return self.name

    def getTeam(self):
        """ getter for player team """
        return self.team

    def getGP(self):
        """ getter for number of games played """
        return self.gp

    def getPoints(self):
        """ getter for number of points """
        return self.pts

    def getRebounds(self):
        """ getter for number of rebounds """
        return self.rbds

    def trade(self, newTeam):
        """ setter for basketball team """
        self.team = newTeam


if __name__ == "__main__":

    p1 = NBAPlayer("Mr. Bloom", 11, "Philadelphia 76ers")
    print(p1)

    p1.playGame(35, 10)
    print(p1)

    p1.trade("New York Knicks")
    print(p1)
