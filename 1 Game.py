'''
class character():
    def __init__(self):
        self.threepoint = 0
        self.midrange = 0
        self.layup = 0
        self.block = 0

    def setThreePointer(self, ThreePointRating):
        self.threepoint = ThreePointRating

    def setMidrange(self, MidrangeRating):
        self.midrange = MidrangeRating

    def setLayup(self, LayupRating):
        self.layup = LayupRating

    def setBlock(self, BlockRating):
        self.block = BlockRating

class court():
    def ShootThreePointer(self):
        if()

'''

import random

#Character's Stats Player 1
CharacterStatsP1 = {'ThreePoint': 0,
                  'Midrange': 0,
                  'Layup': 0,
                  'Outside Block': 0,
                  'Inside Block': 0,
                  'Ball Handle': 0,
                  'Rebound': 0}

#Character's Stats Player 2
CharacterStatsP2 = {'ThreePoint': 0,
                  'Midrange': 0,
                  'Layup': 0,
                  'Outside Block': 0,
                  'Inside Block': 0,
                  'Ball Handle': 0,
                  'Rebound': 0}

#Keeps Track of the Score
PlayerOneScore = 0
PlayerTwoScore = 0

#Keeps Track of Possesion
PlayerOnePossesion = True
PlayerTwoPossesion = False

#Resets all Character's stats to 0
def ResetStatsP1():
    CharacterStatsP1['ThreePoint'] = 0
    CharacterStatsP1['Midrange'] = 0
    CharacterStatsP1['Layup'] = 0
    CharacterStatsP1['Outside Block'] = 0
    CharacterStatsP1['Inside Block'] = 0
    CharacterStatsP1['Ball Handle'] = 0
    CharacterStatsP1['Rebound'] = 0

def ResetStatsP2():
    CharacterStatsP2['ThreePoint'] = 0
    CharacterStatsP2['Midrange'] = 0
    CharacterStatsP2['Layup'] = 0
    CharacterStatsP2['Outside Block'] = 0
    CharacterStatsP2['Inside Block'] = 0
    CharacterStatsP2['Ball Handle'] = 0
    CharacterStatsP2['Rebound'] = 0

#Sets all Character's stats to the same inputted number
def SetAllStatsP1(x):
    CharacterStatsP1['ThreePoint'] = x
    CharacterStatsP1['Midrange'] = x
    CharacterStatsP1['Layup'] = x
    CharacterStatsP1['Outside Block'] = x
    CharacterStatsP1['Inside Block'] = x
    CharacterStatsP1['Ball Handle'] = x
    CharacterStatsP1['Rebound'] = x

def SetAllStatsP2(x):
    CharacterStatsP2['ThreePoint'] = x
    CharacterStatsP2['Midrange'] = x
    CharacterStatsP2['Layup'] = x
    CharacterStatsP2['Outside Block'] = x
    CharacterStatsP2['Inside Block'] = x
    CharacterStatsP2['Ball Handle'] = x
    CharacterStatsP2['Rebound'] = x

#Set's 3 Point rating to the inputted x
def setThreePointerP1(x):
    CharacterStatsP1['ThreePoint'] = x

def setThreePointerP2(x):
    CharacterStatsP2['ThreePoint'] = x

#Set's Midrange rating to the inputted x
def setMidrangeP1(x):
    CharacterStatsP1['Midrange'] = x

def setMidrangeP2(x):
    CharacterStatsP2['Midrange'] = x

#Set's Layup rating to the inputted x
def setLayupP1(x):
    CharacterStatsP1['Layup'] = x

def setLayupP2(x):
    CharacterStatsP2['Layup'] = x

#Set's Inside Block rating to the inputted x
def setInsBlockP1(x):
    CharacterStatsP1['Inside Block'] = x

def setInsBlockP2(x):
    CharacterStatsP2['Inside Block'] = x

#Set's Outside Block rating to the inputted x
def setOutBlockP1(x):
    CharacterStatsP1['Outside Block'] = x

def setOutBlockP2(x):
    CharacterStatsP2['Outside Block'] = x

#Set's Rebound rating to the inputted x
def setReboundP1(x):
    CharacterStatsP1['Rebound'] = x

def setReboundP2(x):
    CharacterStatsP2['Rebound'] = x

#Prints Character Stats
def getCharStatsP1():
    print(CharacterStatsP1)

def getCharStatsP2():
    print(CharacterStatsP2)

'''
def ShootBall():
    if(raw_input('What would you like to do? Shoot a 3 pointer, Midrange shot or Layup? ') == '3 Pointer'):
        ThreePointShot = random.randrange(1,30) + CharacterStats['ThreePoint']
        print(ThreePointShot)

def Defend():
    if(raw_input('What would you like to do? Try a block, steal or grab the rebound? ') == 'Block'):
        BlockAttempt = random.randrange(1,30) + CharacterStats['Block']
        print(BlockAttempt)
'''

#Play Game

def OnePossesion():
    global PlayerOneScore, PlayerTwoScore, PlayerOnePossesion, PlayerTwoPossesion
    print('Player One has the ball!')
    while (PlayerOneScore or PlayerTwoScore <= 11):
        ShootAction = raw_input('What would you like to do? Shoot a 3 pointer, Midrange shot or Layup? ').lower()
        if ((ShootAction == '3 pointer') or (ShootAction == 'midrange') or (ShootAction == 'layup')):
            if (ShootAction == '3 pointer'):
                if (PlayerOnePossesion == True):
                    ThreePointRoll = random.randrange(1, 30) + CharacterStatsP1['ThreePoint']
                    print(ThreePointRoll)
                else:
                    ThreePointRoll = random.randrange(1, 30) + CharacterStatsP2['ThreePoint']
                    print(ThreePointRoll)
                if (raw_input('What would you like to do? Try a block, steal or grab the rebound? ').lower() == 'block'):
                    if (PlayerOnePossesion == True):
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP1['Outside Block']
                        print(BlockRoll)
                    else:
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP2['Outside Block']
                        print(BlockRoll)
                    if (ThreePointRoll < BlockRoll-5):
                        if (PlayerOnePossesion == True):
                            print('You got fully swatted!')
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player Two has the Ball!')
                        elif((PlayerTwoPossesion == True)):
                            print('You got fully swatted!')
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player One has the ball!')
                    if ((ThreePointRoll < BlockRoll) and (ThreePointRoll > BlockRoll-5)):
                        print('The ball got tipped!')
                        ReboundRollP1 = random.randrange(1,30) + CharacterStatsP1['Rebound']
                        print(ReboundRollP1)
                        ReboundRollP2 = random.randrange(1,30) + CharacterStatsP2['Rebound']
                        print(ReboundRollP2)
                        if (ReboundRollP1 > ReboundRollP2):
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player one got the rebound! Player one has the ball.')
                        else:
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player two got the rebound! Player two has the ball.')
                    elif((ThreePointRoll > 28) and (ThreePointRoll > BlockRoll)):
                        print('Splash! You sank the shot!')
                        if(PlayerOnePossesion == True):
                            PlayerOneScore = PlayerOneScore + 3
                        else:
                            PlayerTwoScore = PlayerTwoScore + 3
                        print('Player One Score: ' + str(PlayerOneScore) + ' ,' + 'Player Two Score: ' + str(PlayerTwoScore))
                    elif((ThreePointRoll > 14) and (ThreePointRoll > BlockRoll)):
                        print('Brick! You hit the rim!')
                    elif ((ThreePointRoll < 14) and (ThreePointRoll > BlockRoll)):
                        print('You airballed the shot!')

            elif (ShootAction == 'midrange'):
                if (PlayerOnePossesion == True):
                    MidrangeRoll = random.randrange(1, 30) + CharacterStatsP1['Midrange']
                    print(MidrangeRoll)
                else:
                    MidrangeRoll = random.randrange(1, 30) + CharacterStatsP2['Midrange']
                    print(MidrangeRoll)
                if (raw_input('What would you like to do? Try a block, steal or grab the rebound? ').lower() == 'block'):
                    if (PlayerOnePossesion == True):
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP1['Outside Block']
                        print(BlockRoll)
                    else:
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP2['Outside Block']
                        print(BlockRoll)
                    if (MidrangeRoll < BlockRoll - 5):
                        if (PlayerOnePossesion == True):
                            print('You got fully swatted!')
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player Two has the Ball!')
                        elif ((PlayerTwoPossesion == True)):
                            print('You got fully swatted!')
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player One has the ball!')
                    if ((MidrangeRoll < BlockRoll) and (MidrangeRoll > BlockRoll - 5)):
                        print('The ball got tipped!')
                        ReboundRollP1 = random.randrange(1, 30) + CharacterStatsP1['Rebound']
                        print(ReboundRollP1)
                        ReboundRollP2 = random.randrange(1, 30) + CharacterStatsP2['Rebound']
                        print(ReboundRollP2)
                        if (ReboundRollP1 > ReboundRollP2):
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player one got the rebound! Player one has the ball.')
                        else:
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player two got the rebound! Player two has the ball.')
                    elif ((MidrangeRoll > 22) and (MidrangeRoll > BlockRoll)):
                        print('Splash! You sank the shot!')
                        if (PlayerOnePossesion == True):
                            PlayerOneScore = PlayerOneScore + 2
                        else:
                            PlayerTwoScore = PlayerTwoScore + 2
                        print('Player One Score: ' + str(PlayerOneScore) + ' ,' + 'Player Two Score: ' + str(
                            PlayerTwoScore))
                    elif ((MidrangeRoll > 10) and (MidrangeRoll > BlockRoll)):
                        print('Brick! You hit the rim!')
                        print('You both go for the rebound!')
                        ReboundRollP1 = random.randrange(1, 30) + CharacterStatsP1['Rebound']
                        print(ReboundRollP1)
                        ReboundRollP2 = random.randrange(1, 30) + CharacterStatsP2['Rebound']
                        print(ReboundRollP2)
                        if (ReboundRollP1 > ReboundRollP2):
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player one got the rebound! Player one has the ball.')
                        else:
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player two got the rebound! Player two has the ball.')
                    elif ((MidrangeRoll < 10) and (MidrangeRoll > BlockRoll)):
                        print('You airballed the shot!')
                        if (PlayerOnePossesion == True):
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player Two has the ball.')
                        else:
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player One has the ball.')

            elif (ShootAction == 'layup'):
                if (PlayerOnePossesion == True):
                    LayupRoll = random.randrange(1, 30) + CharacterStatsP1['Layup']
                    print(LayupRoll)
                else:
                    LayupRoll = random.randrange(1, 30) + CharacterStatsP2['Layup']
                    print(LayupRoll)
                if (raw_input(
                        'What would you like to do? Try a block, steal or grab the rebound? ').lower() == 'block'):
                    if (PlayerOnePossesion == True):
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP1['Inside Block']
                        print(BlockRoll)
                    else:
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP2['Inside Block']
                        print(BlockRoll)
                    if (LayupRoll < BlockRoll - 5):
                        if (PlayerOnePossesion == True):
                            print('You got fully swatted!')
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player Two has the Ball!')
                        elif ((PlayerTwoPossesion == True)):
                            print('You got fully swatted!')
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player One has the ball!')
                    if ((LayupRoll < BlockRoll) and (LayupRoll > BlockRoll - 5)):
                        print('The ball got tipped!')
                        ReboundRollP1 = random.randrange(1, 30) + CharacterStatsP1['Rebound']
                        ReboundRollP2 = random.randrange(1, 30) + CharacterStatsP2['Rebound']
                        if (ReboundRollP1 > ReboundRollP2):
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player one got the rebound! Player one has the ball.')
                        else:
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player two got the rebound! Player two has the ball.')
                    elif ((LayupRoll > 16) and (LayupRoll > BlockRoll)):
                        print('Swish! Nice Finish!')
                        if (PlayerOnePossesion == True):
                            PlayerOneScore = PlayerOneScore + 2
                        else:
                            PlayerTwoScore = PlayerTwoScore + 2
                        print('Player One Score: ' + str(PlayerOneScore) + ' ,' + 'Player Two Score: ' + str(
                            PlayerTwoScore))
                    elif ((LayupRoll < 16) and (LayupRoll > BlockRoll)):
                        print('You missed the layup!')
                        print('You both go for the rebound!')
                        ReboundRollP1 = random.randrange(1, 30) + CharacterStatsP1['Rebound']
                        ReboundRollP2 = random.randrange(1, 30) + CharacterStatsP2['Rebound']
                        if (ReboundRollP1 > ReboundRollP2):
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player one got the rebound! Player one has the ball.')
                        else:
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player two got the rebound! Player two has the ball.')
        else:
            print('That is not an option. The three options are 3 pointer, midrange or layup.')

        if (PlayerOneScore >= 11):
            print('Player One Wins!')
            break
        if (PlayerTwoScore >= 11):
            print('Player Two Wins!')
            break


OnePossesion()

