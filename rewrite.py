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
        if (shot == 'three pointer'):
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

class Court1v1():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.PlayerOnePossession = True
        self.PlayerTwoPossession = False
        self.CourtSizeX = 5
        self.CourtSizeY = 5

        self.PlayerOneLocation = {'x': 3, 'y': 1}
        self.PlayerTwoLocation = {'x': 3, 'y': 2}
        self.CurrentPlayerLocation = {'x': 0, 'y': 0}
        self.OtherPlayerLocation = {'x': 0, 'y': 0}
        self.Graphic = {'15': '[ ]', '25': '[ ]', '35': '[ ]', '45': '[ ]', '55': '[ ]',
                        '14': '[ ]', '24': '[ ]', '34': '[ ]', '44': '[ ]', '54': '[ ]',
                        '13': '[ ]', '23': '[ ]', '33': '[ ]', '43': '[ ]', '53': '[ ]',
                        '12': '[ ]', '22': '[ ]', '32': '[ ]', '42': '[ ]', '52': '[ ]',
                        '11': '[ ]', '21': '[ ]', '31': '[ ]', '41': '[ ]', '51': '[ ]', }
        self.x = 1
        self.y = 5
        self.counter = 0

    def SwitchUserLocation(self):
        if (self.PlayerOnePossession == True):
            self.CurrentPlayerLocation = self.PlayerOneLocation
            self.OtherPlayerLocation = self.PlayerTwoLocation
        elif (self.PlayerTwoPossession == True):
            self.CurrentPlayerLocation = self.PlayerTwoLocation
            self.OtherPlayerLocation = self.PlayerOneLocation

    def CreateGraphic(self):
        self.Graphic[(str(self.PlayerOneLocation['x']) + str(self.PlayerOneLocation['y']))] = '[x]'
        self.Graphic[(str(self.PlayerTwoLocation['x']) + str(self.PlayerTwoLocation['y']))] = '[O]'

        print(self.Graphic['15'] + self.Graphic['25'] + self.Graphic['35'] + self.Graphic['45'] + self.Graphic['55'])
        print(self.Graphic['14'] + self.Graphic['24'] + self.Graphic['34'] + self.Graphic['44'] + self.Graphic['54'])
        print(self.Graphic['13'] + self.Graphic['23'] + self.Graphic['33'] + self.Graphic['43'] + self.Graphic['53'])
        print(self.Graphic['12'] + self.Graphic['22'] + self.Graphic['32'] + self.Graphic['42'] + self.Graphic['52'])
        print(self.Graphic['11'] + self.Graphic['21'] + self.Graphic['31'] + self.Graphic['41'] + self.Graphic['51'])

    def Move(self, move):
        self.SwitchUserLocation()
        self.Graphic[(str(self.CurrentPlayerLocation['x']) + str(self.CurrentPlayerLocation['y']))] = '[ ]'
        print(move)
        if((move == 'forward') or (move == 'backward') or (move == 'right') or (move == 'left')):
            print('yes')

            if (move == 'forward'):
                if (self.CurrentPlayerLocation['y'] < 5):
                    self.CurrentPlayerLocation['y'] = self.CurrentPlayerLocation['y'] + 1
                    if(self.OtherPlayerLocation == self.CurrentPlayerLocation):
                        print('You cannot move forward!')
                        self.CurrentPlayerLocation['y'] = self.CurrentPlayerLocation['y'] - 1
                    else:
                        print('You moved forward!')
                elif (self.CurrentPlayerLocation['y'] == 5):
                    print('You cannot move forward!')

            if (move == 'backward'):
                if (self.CurrentPlayerLocation['y'] > 1):
                    self.CurrentPlayerLocation['y'] = self.CurrentPlayerLocation['y'] - 1
                    if (self.OtherPlayerLocation == self.CurrentPlayerLocation):
                        print('You cannot move backward!')
                        self.CurrentPlayerLocation['y'] = self.CurrentPlayerLocation['y'] + 1
                    else:
                        print('You moved backward!')
                elif (self.CurrentPlayerLocation['y'] == 1):
                    print('You cannot move forward!')

            if (move == 'right'):
                if (self.CurrentPlayerLocation['x'] < 5):
                    self.CurrentPlayerLocation['x'] = self.CurrentPlayerLocation['x'] + 1
                    if(self.OtherPlayerLocation == self.CurrentPlayerLocation):
                        print('You cannot move right!')
                        self.CurrentPlayerLocation['x'] = self.CurrentPlayerLocation['x'] - 1
                    else:
                        print('You moved right!')
                elif (self.CurrentPlayerLocation['x'] == 5):
                    print('You cannot move right!')

            if (move == 'left'):
                if (self.CurrentPlayerLocation['x'] > 1):
                    self.CurrentPlayerLocation['x'] = self.CurrentPlayerLocation['x'] - 1
                    if (self.OtherPlayerLocation == self.CurrentPlayerLocation):
                        print('You cannot move left!')
                        self.CurrentPlayerLocation['x'] = self.CurrentPlayerLocation['x'] + 1
                    else:
                        print('You moved left!')
                elif (self.CurrentPlayerLocation['x'] == 1):
                    print('You cannot move left!')
        else:
            print('That is not a valid option')

    def GetScore(self):
        print(p1.name + ': ' + str(self.score1) + ', ' + p2.name + ': ' + str(self.score2))

    def OffenseMain(self):
        if (self.PlayerOnePossession == True):
            OffenseAction = input(
                'What would you like to do ' + p1.name + '? Shoot or Move? ').lower()
            return OffenseAction
        if (self.PlayerTwoPossession == True):
            OffenseAction = input(
                'What would you like to do ' + p2.name + '? Shoot or Move? ').lower()
            return OffenseAction

    def DefenseMain(self):
        if (self.PlayerOnePossession == True):
            DefenseAction = input(
                'What would you like to do ' + p1.name + '? Defend or Move? ').lower()
        if (self.PlayerTwoPossession == True):
            DefenseAction = input(
                'What would you like to do ' + p2.name + '? Defend or Move? ').lower()

    def RollThreePointer(self):
        ThreePointRoll = 0
        if (self.PlayerOnePossession == True):
            p1.Shoot('three pointer')
            ThreePointRoll = p1.Roll__
        else:
            p2.Shoot('three pointer')
            ThreePointRoll = p2.Roll__
        return ThreePointRoll

    def RollMidrange(self):
        MidrangeRoll = 0
        if (self.PlayerOnePossession == True):
            p1.Shoot('midrange')
            MidrangeRoll = p1.Roll__
        else:
            p2.Shoot('midrange')
            MidrangeRoll = p2.Roll__
        return MidrangeRoll

    def RollLayup(self):
        LayupRoll = 0
        if (self.PlayerOnePossession == True):
            p1.Shoot('layup')
            LayupRoll = p1.Roll__
        else:
            p2.Shoot('layup')
            LayupRoll = p2.Roll__
        return LayupRoll

    def RollOutsideBlock(self):
        BlockRoll = 0
        if (self.PlayerOnePossession == True):
            p2.Defend('outside block')
            BlockRoll = p2.Roll__
        else:
            p1.Defend('outside block')
            BlockRoll = p1.Roll__
        return BlockRoll

    def GrabRebound(self):
        p1.Defend('rebound')
        ReboundRollP1 = p1.Roll__
        p2.Defend('rebound')
        ReboundRollP2 = p2.Roll__
        if (ReboundRollP1 > ReboundRollP2):
            Court1v1.SwitchPossesion
            print(p1.name + ' got the rebound! ' + p1.name + ' has the ball.')
        else:
            Court1v1.SwitchPossesion
            print(p2.name + ' got the rebound! ' + p2.name + ' has the ball.')

    def SwitchPossesion(self):
        if(self.PlayerOnePossession == True):
            self.PlayerOnePossession = False
            self.PlayerTwoPossession = True
        else:
            self.PlayerOnePossession = True
            self.PlayerTwoPossession = False

    def ScoreThreePoint(self):
        if (self.PlayerOnePossession == True):
            print('Splash! ' + p1.name + '  sank the shot!')
            self.score1 = self.score1 + 3
        else:
            print('Splash! ' + p2.name + '  sank the shot!')
            self.score2 = self.score2 + 3

    def AirballShot(self):
        if (self.PlayerOnePossession == True):
            print(p1.name + ' airballed the shot!')
            Court1v1.SwitchPossesion(self)
            print(p2.name + ' now has the ball.')
        else:
            print(p2.name + ' airballed the shot!')
            Court1v1.SwitchPossesion(self)
            print(p1.name + ' now has the ball.')

    def PlayGame(self):
        print(p1.name + ' has the ball! (P1 is X, P2 is O)')
        self.CreateGraphic()
        while (self.score1 or self.score2 <= 11):
            Court1v1.SwitchUserLocation(self)
            OffenseAction = Court1v1.OffenseMain(self)
            if(OffenseAction == 'shoot'):
                if((self.CurrentPlayerLocation['x'] == 3) and (self.CurrentPlayerLocation['y'] == 3 or 4 or 5)):
                    LayupRoll = Court1v1.RollLayup(self)
                    print(LayupRoll)
                elif (((self.CurrentPlayerLocation['x'] == 2 or 4) and (
                        self.CurrentPlayerLocation['y'] == 1 or 2 or 3 or 4) or (
                               (self.CurrentPlayerLocation['x'] == 3) and (self.CurrentPlayerLocation['y'] == 2)))):
                    MidrangeRoll = Court1v1.RollMidrange(self)
                    print(MidrangeRoll)
                elif((self.CurrentPlayerLocation['x'] == 1) or (self.CurrentPlayerLocation['y'] == 1) or (self.CurrentPlayerLocation['x'] == 5)):
                    ThreePointRoll = Court1v1.RollThreePointer(self)
                    print(ThreePointRoll)
            elif(OffenseAction == 'move'):
                move = input('Which direction do you want move in? ')
                print(move)
                Court1v1.Move(self, move)
                Court1v1.CreateGraphic(self)
                Court1v1.SwitchPossesion(self)

            #DefenseAction = Court1v1.DefenseMain(self)

            if (self.score1 >= 11):
                print(p1.name + ' won!')
                break
            if (self.score2 >= 11):
                print(p2.name + ' won!')
                break


# Assign's Classes to Objects
Court11v1 = Court1v1()
p1 = Player('Player 1')
p2 = Player('Player 2')

# Actions
p1.setRating('ThreePoint__', 20)
p2.setRating('ThreePoint__', 20)
#ourt11v1.PlayGame()

a = Court1v1()
a.PlayGame()