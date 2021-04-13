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

class Court1v1():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.PlayerOnePossession = True
        self.PlayerTwoPossession = False
        self.CourtSizeX = 5
        self.CourtSizeY = 5

    def GetScore(self):
        print('The score is, Player 1: ' + str(self.score1) + ', ' + 'Player 2: ' + str(self.score2))

    def PlayGame(self):
        print(p1.name + ' has the ball!')
        while (self.score1 or self.score2 <= 11):
            if (self.PlayerOnePossession == True):
                ShootAction = input('What would you like to do ' + p1.name + '? Shoot a 3 pointer, Midrange shot or Layup? ').lower()
            if (self.PlayerTwoPossession == True):
                ShootAction = input('What would you like to do ' + p2.name + '? Shoot a 3 pointer, Midrange shot or Layup? ').lower()
            if ((ShootAction == '3 pointer') or (ShootAction == 'midrange') or (ShootAction == 'layup')):
                if (ShootAction == '3 pointer'):
                    if (self.PlayerOnePossession == True):
                        p1.Shoot('3 pointer')
                        ThreePointRoll = p1.Roll__
                    else:
                        p2.Shoot('3 pointer')
                        ThreePointRoll = p2.Roll__
                    if (self.PlayerOnePossession == True):
                        BlockAttempt = input(p2.name + ', Would you like to try to block the shot or go rebound? ').lower()
                    else:
                        BlockAttempt = input(p1.name + ', Would you like to try to block the shot or go rebound? ').lower()
                    if (BlockAttempt == 'block'):
                        if (self.PlayerOnePossession == True):
                            p2.Defend('outside block')
                            BlockRoll = p2.Roll__
                        else:
                            p1.Defend('outside block')
                            BlockRoll = p1.Roll__
                        if (ThreePointRoll < BlockRoll - 5):
                            if (self.PlayerOnePossession == True):
                                print(p1.name + ' got fully swatted!')
                                self.PlayerOnePossession = False
                                self.PlayerTwoPossession = True
                                print(p2.name + ' has the Ball!')
                            elif ((self.PlayerTwoPossession == True)):
                                print(p2.name + ' got fully swatted!')
                                self.PlayerOnePossession = True
                                self.PlayerTwoPossession = False
                                print(p1.name + ' has the ball!')
                        if ((ThreePointRoll < BlockRoll) and (ThreePointRoll > BlockRoll - 5)):
                            print('The ball got tipped!')
                            print('You both jump for the rebound!')
                            p1.Defend('rebound')
                            ReboundRollP1 = p1.Roll__
                            p2.Defend('rebound')
                            ReboundRollP2 = p2.Roll__
                            if (ReboundRollP1 > ReboundRollP2):
                                self.PlayerOnePossession = True
                                self.PlayerTwoPossession = False
                                print(p1.name + ' got the rebound! ' + p1.name + ' has the ball.')
                            else:
                                self.PlayerOnePossession = False
                                self.PlayerTwoPossession = True
                                print(p2.name + ' got the rebound! ' + p2.name + ' has the ball.')
                        elif ((ThreePointRoll > 28) and (ThreePointRoll > BlockRoll)):
                            if (self.PlayerOnePossession == True):
                                print('Splash! ' + p1.name + '  sank the shot!')
                                self.score1 = self.score1 + 3
                            else:
                                self.score2 = self.score2 + 3
                            print(p1.name + ' Score: ' + str(self.score1) + ' ,' + p2.name + ' Score: ' + str(self.score2))
                        elif ((ThreePointRoll > 14) and (ThreePointRoll > BlockRoll)):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' hit the rim!')
                            else:
                                print('Brick! ' + p2.name + ' hit the rim!')
                            print('You both run to the paint and jump for the rebound!')
                            p1.Defend('rebound')
                            ReboundRollP1 = p1.Roll__
                            p2.Defend('rebound')
                            ReboundRollP2 = p2.Roll__
                            if (ReboundRollP1 > ReboundRollP2):
                                self.PlayerOnePossession = True
                                self.PlayerTwoPossession = False
                                print(p1.name + ' got the rebound! ' + p1.name + ' has the ball.')
                            else:
                                self.PlayerOnePossession = False
                                self.PlayerTwoPossession = True
                                print(p2.name + ' got the rebound! ' + p2.name + ' has the ball.')
                        elif ((ThreePointRoll < 14) and (ThreePointRoll > BlockRoll)):
                            print('You airballed the shot!')
                            if (self.PlayerOnePossession == True):
                                print(p1.name + ' airballed the shot!')
                                self.PlayerOnePossession = False
                                self.PlayerTwoPossession = True
                                print(p2.name + ' now has the ball.')
                            else:
                                print(p2.name + ' airballed the shot!')
                                self.PlayerOnePossession = True
                                self.PlayerTwoPossession = False
                                print(p1.name + ' now has the ball.')
                    elif (BlockAttempt == 'rebound'):
                        if (ThreePointRoll > 28):
                            if (self.PlayerOnePossession == True):
                                print('Splash! ' + p1.name + '  sank the shot!')
                                self.score1 = self.score1 + 3
                            else:
                                print('Splash! ' + p2.name + '  sank the shot!')
                                self.score2 = self.score2 + 3
                                print(p1.name + ' Score: ' + str(self.score1) + ' ,' + p2.name + ' Score: ' + str(self.score2))
                        elif (ThreePointRoll > 14):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' You hit the rim!')
                                print(p2.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                self.PlayerOnePossession = False
                                self.PlayerTwoPossession = True
                            else:
                                print('Brick! ' + p2.name + ' You hit the rim!')
                                print(p1.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                self.PlayerOnePossession = True
                                self.PlayerTwoPossession = False
                        elif (ThreePointRoll < 14):
                            if (self.PlayerOnePossession == True):
                                print(p1.name + ', YOU AIRBALLED THE SHOT!')
                                print(p2.name + ' now has the ball.')
                                self.PlayerOnePossession = False
                                self.PlayerTwoPossession = True
                            else:
                                print(p2.name + ', YOU AIRBALLED THE SHOT!')
                                print(p1.name + ' now has the ball.')
                                self.PlayerOnePossession = True
                                self.PlayerTwoPossession = False
            else:
                print('That is not an option. The three options are 3 pointer, midrange or layup.')

            if (self.score1 >= 11):
                print(p1.name + ' won!')
                break
            if (self.score2 >= 11):
                print(p2.name + ' won!')
                break

#Assign's Classes to Objects
Court11v1 = Court1v1()
p1 = Player('Square')
p2 = Player('Chunky')

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

    def CreateGraphic(self):
        self.Graphic[(str(self.PlayerOneLocation['x']) + str(self.PlayerOneLocation['y']))] = '[x]'

        print(self.Graphic['15'] + self.Graphic['25'] + self.Graphic['35'] + self.Graphic['45'] + self.Graphic['55'])
        print(self.Graphic['14'] + self.Graphic['24'] + self.Graphic['34'] + self.Graphic['44'] + self.Graphic['54'])
        print(self.Graphic['13'] + self.Graphic['23'] + self.Graphic['33'] + self.Graphic['43'] + self.Graphic['53'])
        print(self.Graphic['12'] + self.Graphic['22'] + self.Graphic['32'] + self.Graphic['42'] + self.Graphic['52'])
        print(self.Graphic['11'] + self.Graphic['21'] + self.Graphic['31'] + self.Graphic['41'] + self.Graphic['51'])

    def Move(self, move):
        self.Graphic[(str(self.PlayerOneLocation['x']) + str(self.PlayerOneLocation['y']))] = '[ ]'
        if (move == 'forward'):
            if (self.PlayerOneLocation['y'] < 5):
                print('You moved forward!')
                self.PlayerOneLocation['y'] = self.PlayerOneLocation['y'] + 1
            elif (self.PlayerOneLocation['y'] == 5):
                print('You cannot move forward!')
        if (move == 'backward'):
            if (self.PlayerOneLocation['y'] > 1):
                print('You moved backward!')
                self.PlayerOneLocation['y'] = self.PlayerOneLocation['y'] - 1
            elif (self.PlayerOneLocation['y'] == 1):
                print('You cannot move backward!')
        if (move == 'right'):
            if (self.PlayerOneLocation['x'] < 5):
                print('You moved right!')
                self.PlayerOneLocation['x'] = self.PlayerOneLocation['x'] + 1
            elif (self.PlayerOneLocation['x'] == 5):
                print('You cannot move right!')
        if (move == 'left'):
            if (self.PlayerOneLocation['x'] > 1):
                print('You moved left!')
                self.PlayerOneLocation['x'] = self.PlayerOneLocation['x'] - 1
            elif (self.PlayerOneLocation['x'] == 1):
                print('You cannot move left!')

#Actions
p1.SetThreePointRating(20)
p2.SetThreePointRating(20)
Court11v1.PlayGame()

a = Location()
a.CreateGraphic()
a.Move('left')