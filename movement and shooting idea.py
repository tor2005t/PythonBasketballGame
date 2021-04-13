import random

class Location():
    def __init__(self):
        self.PlayerOneLocation = {'x': 3, 'y': 1}
        self.Graphic = {'15': '[ ]', '25': '[ ]', '35': '[ ]', '45': '[ ]', '55': '[ ]',
                        '14': '[ ]', '24': '[ ]', '34': '[ ]', '44': '[ ]', '54': '[ ]',
                        '13': '[ ]', '23': '[ ]', '33': '[ ]', '43': '[ ]', '53': '[ ]',
                        '12': '[ ]', '22': '[ ]', '32': '[ ]', '42': '[ ]', '52': '[ ]',
                        '11': '[ ]', '21': '[ ]', '31': '[ ]', '41': '[ ]', '51': '[ ]',}
        self.x = 1
        self.y = 5
        self.counter = 0

class Court1v1():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.PlayerOnePossession = True
        self.PlayerTwoPossession = False
        self.CourtSizeX = 5
        self.CourtSizeY = 5

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

    def Shoot(self, shot):
        if (shot == '3 pointer'):
            self.Roll__ = random.randrange(1, 30) + self.ThreePoint__
        if (shot == 'midrange'):
            self.Roll__ = random.randrange(1, 30) + self.Midrange__
        if (shot == 'layup'):
            self.Roll__ = random.randrange(1, 30) + self.Layup__

    def Defend(self, defense):
        if (defense == 'outside block'):
            self.Roll__ = random.randrange(1, 30) + self.OutsideBlock__
        if (defense == 'inside block'):
            self.Roll__ = random.randrange(1, 30) + self.InsideBlock__
        if (defense == 'rebound'):
            self.Roll__ = random.randrange(1, 30) + self.Rebound__
        if (defense == 'steal'):
            self.Roll__ = random.randrange(1, 30) + self.Steal__


c = Court1v1()
p = Player('Tor')
z = Location()
if (c.PlayerOnePossession == True):
    if ((z.PlayerOneLocation['y'] == 1) or (z.PlayerOneLocation['x'] == 1) or (z.PlayerOneLocation['x'] == 5)):
        moveorshoot = input('Would you like to move or shoot?: ')
        if(moveorshoot == 'move'):
            input()
        if(moveorshoot == 'shoot'):
            print('n')

'''
Logic:
1. Check Attacker Position(coordinates) on Court
2. Check Options based on Position
  - 3pt Area = Shoot or Move (3pt)
  - Midrange Area = Shoot or Move (2pt)
  - Paint Area = Layup or Move (2pt)
3. Check Defender Position(coordinates) on Court
4. Check Options based on Position + Offensive Action
  - Attacker Moves
    * 3pt Area = Move or Steal (within 1 block radius)
    * Midrange Area = Move or Steal (within 1 block radius)
    * Paint Area = Move or Steal (within 1 block radius)
  - Attacker Shoots
    * 3pt Area = Move/Rebound (sag off defender) or Block (within 1 block radius)
    * Midrange Area = Move/Rebound (sag off defender) or Block (within 1 block radius)
    * Paint Area = Block (within 1 block radius)
5. Execute Action
  - Roll Dice Based on Scenario etc.
6. 
'''

