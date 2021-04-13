import random
class Player():
    def __init__(self,name):
        self.name = name
        self.ThreePoint__ = 0
        self.Midrange__ = 0
        self.Layup__ = 0
        self.OutsideBlock__ = 0
        self.InsideBlock__ = 0
        self.BallHandle__ = 0
        self.Rebound__ = 0
        self.Steal__ = 0
        self.Roll__ = 0

    def printRating(self,option,score):
        print(option +" Rating has been set to: " + str(score))

    def setRating(self,option,score):
        if option == "Three point":
            self.ThreePoint__ = score
        elif option == "Midrange":
            self.Midrange__ = score
        elif option == "Outside Block":
            self.OutsideBlock__ = score
        elif option == "Inside Block":
            self.InsideBlock__ = score
        elif option == "Ball Handling":
            self.BallHandle__ = score
        elif option == "Rebounding":
            self.Rebound__ = score
        elif option == "Steal":
            self.Steal__ = score
        else:
            print("Option is not in the list, please select the new option")
        Player.printRating(self, option, score)

    def Shoot(self, shot):
        if (shot == '3 pointer'):
            self.Roll__ = random.randrange(1,30) + self.ThreePoint__
        if (shot == 'midrange'):
            self.Roll__ = random.randrange(1,30) + self.Midrange__
        if (shot == 'layup'):
            self.Roll__ = random.randrange(1,30) + self.Layup__

    def Defend(self, defense):
        if (defense == 'outside block'):
            self.Roll__ = random.randrange(1,30) + self.OutsideBlock__
        elif (defense == 'inside block'):
            self.Roll__ = random.randrange(1,30) + self.InsideBlock__
        elif (defense == 'rebound'):
            self.Roll__ = random.randrange(1,30) + self.Rebound__
        elif (defense == 'steal'):
            self.Roll__ = random.randrange(1,30) + self.Steal__




