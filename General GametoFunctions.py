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
        return self.Roll__

    def Defend(self, defense):
        if (defense == 'outside block'):
            self.Roll__ = random.randrange(1,30) + self.OutsideBlock__
        elif (defense == 'inside block'):
            self.Roll__ = random.randrange(1,30) + self.InsideBlock__
        elif (defense == 'rebound'):
            self.Roll__ = random.randrange(1,30) + self.Rebound__
        elif (defense == 'steal'):
            self.Roll__ = random.randrange(1,30) + self.Steal__
        return self.Roll__

class Court1v1():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.PlayerOnePossession = True
        self.PlayerTwoPossession = False
        self.CourtSizeX = 5
        self.CourtSizeY = 5

    def GetScore(self):
        print(p1.name + ': ' + str(self.score1) + ', ' + p2.name + ': ' + str(self.score2))

    def OffenseQuestion(self):
        if (self.PlayerOnePossession == True):
            ShootAction = input(
                'What would you like to do ' + p1.name + '? Shoot a 3 pointer, Midrange shot or Layup? ').lower()
        if (self.PlayerTwoPossession == True):
            ShootAction = input(
                'What would you like to do ' + p2.name + '? Shoot a 3 pointer, Midrange shot or Layup? ').lower()
        return ShootAction

    def DefenseQuestion(self):
        if (self.PlayerOnePossession == True):
            BlockAttempt = input(p2.name + ', Would you like to try to block the shot or go rebound? ').lower()
        else:
            BlockAttempt = input(p1.name + ', Would you like to try to block the shot or go rebound? ').lower()
        return BlockAttempt

    def RollShot(self):
        ThreePointRoll = 0
        if (self.PlayerOnePossession == True):
            ThreePointRoll =  p1.Shoot('3 pointer')
        else:
            ThreePointRoll = p2.Shoot('3 pointer')
        return ThreePointRoll

    def RollOutsideBlock(self):
        BlockRoll = 0
        if (self.PlayerOnePossession == True):
            BlockRoll = p2.Defend('outside block')
        else:
            BlockRoll = p1.Defend('outside block')
        return BlockRoll

    def GrabRebound(self):
        ReboundRollP1 = p1.Defend('rebound')
        ReboundRollP2 = p2.Defend('rebound')
        if (ReboundRollP1 > ReboundRollP2):
            Court1v1.SwitchPossesionP1
            print(p1.name + ' got the rebound! ' + p1.name + ' has the ball.')
        else:
            Court1v1.SwitchPossesionP2
            print(p2.name + ' got the rebound! ' + p2.name + ' has the ball.')

    def SwitchPossesionP2(self):
        self.PlayerOnePossession = False
        self.PlayerTwoPossession = True

    def SwitchPossesionP1(self):
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
            Court1v1.SwitchPossesionP2(self)
            print(p2.name + ' now has the ball.')
        else:
            print(p2.name + ' airballed the shot!')
            Court1v1.SwitchPossesionP1(self)
            print(p1.name + ' now has the ball.')

    def PlayGame(self):
        print(p1.name + ' has the ball!')
        while (self.score1 or self.score2 <= 11):
            ShootAction = Court1v1.OffenseQuestion(self)
            if ((ShootAction == '3 pointer') or (ShootAction == 'midrange') or (ShootAction == 'layup')):
                if (ShootAction == '3 pointer'):
                    ThreePointRoll = Court1v1.RollShot(self)
                    BlockAttempt = Court1v1.DefenseQuestion(self)
                    if (BlockAttempt == 'block'):
                        BlockRoll = Court1v1.RollOutsideBlock(self)
                        if (ThreePointRoll < BlockRoll - 5):
                            if (self.PlayerOnePossession == True):
                                print(p1.name + ' got fully swatted!')
                                Court1v1.SwitchPossesionP2(self)
                                print(p2.name + ' has the Ball!')
                            elif ((self.PlayerTwoPossession == True)):
                                print(p2.name + ' got fully swatted!')
                                Court1v1.SwitchPossesionP1(self)
                                print(p1.name + ' has the ball!')
                        if ((ThreePointRoll < BlockRoll) and (ThreePointRoll > BlockRoll - 5)):
                            print('The ball got tipped!')
                            print('You both jump for the rebound!')
                            Court1v1.GrabRebound(self)
                        elif ((ThreePointRoll > 28) and (ThreePointRoll > BlockRoll)):
                            Court1v1.ScoreThreePoint(self)
                            Court1v1.GetScore(self)
                        elif ((ThreePointRoll > 14) and (ThreePointRoll > BlockRoll)):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' hit the rim!')
                            else:
                                print('Brick! ' + p2.name + ' hit the rim!')
                            print('You both run to the paint and jump for the rebound!')
                            Court1v1.GrabRebound(self)
                        elif ((ThreePointRoll < 14) and (ThreePointRoll > BlockRoll)):
                            Court1v1.AirballShot(self)
                    elif (BlockAttempt == 'rebound'):
                        if (ThreePointRoll > 28):
                            Court1v1.ScoreThreePoint(self)
                            Court1v1.GetScore(self)
                        elif (ThreePointRoll > 14):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' You hit the rim!')
                                print(p2.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                Court1v1.SwitchPossesionP2(self)
                            else:
                                print('Brick! ' + p2.name + ' You hit the rim!')
                                print(p1.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                Court1v1.SwitchPossesionP1(self)
                        elif (ThreePointRoll < 14):
                            Court1v1.AirballShot(self)
                if (ShootAction == 'midrange'):
                    MidrangeRoll = Court1v1.RollShot(self)
                    BlockAttempt = Court1v1.DefenseQuestion(self)
                    if (BlockAttempt == 'block'):
                        BlockRoll = Court1v1.RollOutsideBlock(self)
                        if (MidrangeRoll < BlockRoll - 5):
                            if (self.PlayerOnePossession == True):
                                print(p1.name + ' got fully swatted!')
                                Court1v1.SwitchPossesionP2(self)
                                print(p2.name + ' has the Ball!')
                            elif ((self.PlayerTwoPoss ession == True)):
                                print(p2.name + ' got fully swatted!')
                                Court1v1.SwitchPossesionP1(self)
                                print(p1.name + ' has the ball!')
                        if ((MidrangeRoll < BlockRoll) and (MidrangeRoll > BlockRoll - 5)):
                            print('The ball got tipped!')
                            print('You both jump for the rebound!')
                            Court1v1.GrabRebound(self)
                        elif ((MidrangeRoll > 22) and (MidrangeRoll > BlockRoll)):
                            Court1v1.ScoreThreePoint(self)
                            Court1v1.GetScore(self)
                        elif ((MidrangeRoll > 10) and (MidrangeRoll > BlockRoll)):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' hit the rim!')
                            else:
                                print('Brick! ' + p2.name + ' hit the rim!')
                            print('You both run to the paint and jump for the rebound!')
                            Court1v1.GrabRebound(self)
                        elif ((MidrangeRoll < 10) and (MidrangeRoll > BlockRoll)):
                            Court1v1.AirballShot(self)
                    elif (BlockAttempt == 'rebound'):
                        if (MidrangeRoll > 22):
                            Court1v1.ScoreThreePoint(self)
                            Court1v1.GetScore(self)
                        elif (MidrangeRoll > 10):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' You hit the rim!')
                                print(p2.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                Court1v1.SwitchPossesionP2(self)
                            else:
                                print('Brick! ' + p2.name + ' You hit the rim!')
                                print(p1.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                Court1v1.SwitchPossesionP1(self)
                        elif (MidrangeRoll < 10):
                            Court1v1.AirballShot(self)
                if (ShootAction == 'layup'):
                    LayupRoll = Court1v1.RollShot(self)
                    BlockAttempt = w
                    if (BlockAttempt == 'block'):
                        BlockRoll = Court1v1.RollOutsideBlock(self)
                        if (LayupRoll < BlockRoll - 5):
                            if (self.PlayerOnePossession == True):
                                print(p1.name + ' got fully swatted!')
                                Court1v1.SwitchPossesionP2(self)
                                print(p2.name + ' has the Ball!')
                            elif ((self.PlayerTwoPossession == True)):
                                print(p2.name + ' got fully swatted!')
                                Court1v1.SwitchPossesionP1(self)
                                print(p1.name + ' has the ball!')
                        if ((LayupRoll < BlockRoll) and (LayupRoll > BlockRoll - 5)):
                            print('The ball got tipped!')
                            print('You both jump for the rebound!')
                            Court1v1.GrabRebound(self)
                        elif ((LayupRoll > 28) and (LayupRoll > BlockRoll)):
                            Court1v1.ScoreThreePoint(self)
                            Court1v1.GetScore(self)
                        elif ((LayupRoll > 14) and (LayupRoll > BlockRoll)):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' hit the rim!')
                            else:
                                print('Brick! ' + p2.name + ' hit the rim!')
                            print('You both run to the paint and jump for the rebound!')
                            Court1v1.GrabRebound(self)
                        elif ((LayupRoll < 14) and (LayupRoll > BlockRoll)):
                            Court1v1.AirballShot(self)
                    elif (BlockAttempt == 'rebound'):
                        if (LayupRoll > 28):
                            Court1v1.ScoreThreePoint(self)
                            Court1v1.GetScore(self)
                        elif (LayupRoll > 14):
                            if (self.PlayerOnePossession == True):
                                print('Brick! ' + p1.name + ' You hit the rim!')
                                print(p2.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                Court1v1.SwitchPossesionP2(self)
                            else:
                                print('Brick! ' + p2.name + ' You hit the rim!')
                                print(p1.name + "'s bet paid off. He grabs the rebound and now has the ball.")
                                Court1v1.SwitchPossesionP1(self)
                        elif (LayupRoll < 14):
                            Court1v1.AirballShot(self)
            else:
                print('That is not an option. The three options are 3 pointer, midrange or layup.')

            if (self.score1 >= 11):
                print(p1.name + ' won!')
                break
            if (self.score2 >= 11):
                print(p2.name + ' won!')
                break

# Assign's Classes to Objects
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
                        '11': '[ ]', '21': '[ ]', '31': '[ ]', '41': '[ ]', '51': '[ ]', }
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


# Actions
p1.setRating('ThreePoint__', 20)
p2.setRating('ThreePoint__', 20)
Court11v1.PlayGame()

a = Location()
a.CreateGraphic()
a.Move('left')