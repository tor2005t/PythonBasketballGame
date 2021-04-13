class Court1v1():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.CourtSizeX = 5
        self.CourtSizeY = 5

    def GetScore(self):
        print('The score is, Player 1: ' + str(self.score1) + ', ' + 'Player 2: ' + str(self.score2))

Court11v1 = Court1v1()
Court11v1.GetScore()