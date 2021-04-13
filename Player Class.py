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

    def SetThreePointRating(self, x):
        self.ThreePoint__ = x
        print('Three Point Rating has been set to: ' + str(x))

    def SetMidrangeRating(self, x):
        self.Midrange__ = x
        print('Midrange Rating has been set to: ' + str(x))

    def SetLayupRating(self, x):
        self.Layup__ = x
        print('Layup Rating has been set to: ' + str(x))

    def SetOutsideBlockRating(self, x):
        self.OutsideBlock__ = x
        print('Outside Block Rating has been set to: ' + str(x))

    def SetInsideBlockRating(self, x):
        self.InsideBlock__ = x
        print('Inside Block Rating has been set to: ' + str(x))

    def SetBallHandleRating(self, x):
        self.BallHandle__ = x
        print('Ball Handling Rating has been set to: ' + str(x))

    def SetReboundRating(self, x):
        self.Rebound__ = x
        print('Rebounding Rating has been set to: ' + str(x))

    def SetStealRating(self, x):
        self.Steal__ = x
        print('Steal Rating has been set to: ' + str(x))

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
        if (defense == 'inside block'):
            self.Roll__ = random.randrange(1,30) + self.InsideBlock__
        if (defense == 'rebound'):
            self.Roll__ = random.randrange(1,30) + self.Rebound__
        if (defense == 'steal'):
            self.Roll__ = random.randrange(1,30) + self.Steal__



'''
        self.ThreePointRoll__ = 0
        self.MidrangeRoll__ = 0
        self.LayupRoll__ = 0
        self.OutsideBlockRoll__ = 0
        self.InsideBlockRoll__ = 0
        self.ReboundRoll__ = 0
'''

'''
    def ThreePointShot(self):
        self.ThreePointRoll__ = random.randrange(1, 30) + self.ThreePoint__
        return self.ThreePointRoll__

    def MidrangeShot(self):
        self.MidrangeRoll__ = random.randrange(1, 30) + self.Midrange__
        return self.MidrangeRoll__

    def LayupShot(self):
        self.LayupRoll__ = random.randrange(1, 30) + self.Layup__
        return self.LayupRoll__

    def OutsideDefense(self):
        self.OutsideBlockRoll__ = random.randrange(1, 30) + self.OutsideBlock__
        return self.OutsideBlockRoll__

    def InsideBlock(self):
        self.InsideBlockRoll__ = random.randrange(1, 30) + self.InsideBlock
        return self.InsideBlockRoll__

    def Rebound(self):
        self.ReboundRoll__ = random.randrange(1, 30) + self.Rebound__
        return self.ReboundRoll__
'''

p1 = Player('Tor')
p1.Shoot('3 pointer')
print(p1.Roll__)
p2 = Player('Varun')
p2.Defend('outside block')
print(p2.Roll__)



