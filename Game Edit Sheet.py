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

import math
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
    print("Player One's ratings have been reset to 0.")

def ResetStatsP2():
    CharacterStatsP2['ThreePoint'] = 0
    CharacterStatsP2['Midrange'] = 0
    CharacterStatsP2['Layup'] = 0
    CharacterStatsP2['Outside Block'] = 0
    CharacterStatsP2['Inside Block'] = 0
    CharacterStatsP2['Ball Handle'] = 0
    CharacterStatsP2['Rebound'] = 0
    print("Player Two's ratings have been reset to 0.")

#Sets all Character's stats to the same inputted number
def SetAllStatsP1(x):
    CharacterStatsP1['ThreePoint'] = x
    CharacterStatsP1['Midrange'] = x
    CharacterStatsP1['Layup'] = x
    CharacterStatsP1['Outside Block'] = x
    CharacterStatsP1['Inside Block'] = x
    CharacterStatsP1['Ball Handle'] = x
    CharacterStatsP1['Rebound'] = x
    print("All of Player One's ratings are now " + str(x))

def SetAllStatsP2(x):
    CharacterStatsP2['ThreePoint'] = x
    CharacterStatsP2['Midrange'] = x
    CharacterStatsP2['Layup'] = x
    CharacterStatsP2['Outside Block'] = x
    CharacterStatsP2['Inside Block'] = x
    CharacterStatsP2['Ball Handle'] = x
    CharacterStatsP2['Rebound'] = x
    print("All of Player Two's ratings are now " + str(x))

#Set's 3 Point rating to the inputted x
def setThreePointerP1(x):
    CharacterStatsP1['ThreePoint'] = x
    print("Player One's Three Point rating is now " + str(x))

def setThreePointerP2(x):
    CharacterStatsP2['ThreePoint'] = x
    print("Player Two's Three Point rating is now " + str(x))

#Set's Midrange rating to the inputted x
def setMidrangeP1(x):
    CharacterStatsP1['Midrange'] = x
    print("Player One's Midrange rating is now " + str(x))

def setMidrangeP2(x):
    CharacterStatsP2['Midrange'] = x
    print("Player Two's Midrange rating is now " + str(x))

#Set's Layup rating to the inputted x
def setLayupP1(x):
    CharacterStatsP1['Layup'] = x
    print("Player One's Layup rating is now " + str(x))

def setLayupP2(x):
    CharacterStatsP2['Layup'] = x
    print("Player Two's Layup rating is now " + str(x))

#Set's Inside Block rating to the inputted x
def setInsBlockP1(x):
    CharacterStatsP1['Inside Block'] = x
    print("Player One's Inside Block rating is now " + str(x))

def setInsBlockP2(x):
    CharacterStatsP2['Inside Block'] = x
    print("Player Two's Inside Block rating is now " + str(x))

#Set's Outside Block rating to the inputted x
def setOutBlockP1(x):
    CharacterStatsP1['Outside Block'] = x
    print("Player One's Outside Block rating is now " + str(x))

def setOutBlockP2(x):
    CharacterStatsP2['Outside Block'] = x
    print("Player Two's Outside Block rating is now " + str(x))

#Set's Rebound rating to the inputted x
def setReboundP1(x):
    CharacterStatsP1['Rebound'] = x
    print("Player One's Rebound rating is now " + str(x))

def setReboundP2(x):
    CharacterStatsP2['Rebound'] = x
    print("Player Two's Rebound rating is now " + str(x))

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
                else:
                    ThreePointRoll = random.randrange(1, 30) + CharacterStatsP2['ThreePoint']
                BlockAttempt = raw_input('Would you like to try to block the shot or go rebound? ').lower()
                if (BlockAttempt == 'block'):
                    if (PlayerOnePossesion == True):
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP1['Outside Block']
                    else:
                        BlockRoll = random.randrange(1, 30) + CharacterStatsP2['Outside Block']
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
                        print('You both jump for the rebound!')
                        ReboundRollP1 = random.randrange(1,30) + CharacterStatsP1['Rebound']
                        ReboundRollP2 = random.randrange(1,30) + CharacterStatsP2['Rebound']
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
                        #Add rebounding mechanism
                    elif ((ThreePointRoll < 14) and (ThreePointRoll > BlockRoll)):
                        print('You airballed the shot!')
                        if (PlayerOnePossesion == True):
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                            print('Player Two now has the ball.')
                        else:
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                            print('Player One now has the ball.')
                if (BlockAttempt == 'rebound'):
                    if (ThreePointRoll > 28):
                        print('Splash! You sank the shot!')
                        if (PlayerOnePossesion == True):
                            PlayerOneScore = PlayerOneScore + 3
                        else:
                            PlayerTwoScore = PlayerTwoScore + 3
                        print('Player One Score: ' + str(PlayerOneScore) + ' ,' + 'Player Two Score: ' + str(
                            PlayerTwoScore))
                    elif (ThreePointRoll > 14):
                        print('Brick! You hit the rim!')
                        if (PlayerOnePossesion == True):
                            print("Player Two's bet paid off. They grab the rebound and now have the ball.")
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                        else:
                            print("Player One's bet paid off. They grab the rebound and now have the ball.")
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
                    elif (ThreePointRoll < 14):
                        print('You airballed the shot!')
                        if (PlayerOnePossesion == True):
                            print('Player Two now has the ball.')
                            PlayerOnePossesion = False
                            PlayerTwoPossesion = True
                        else:
                            print('Player One now has the ball.')
                            PlayerOnePossesion = True
                            PlayerTwoPossesion = False
        else:
            print('That is not an option. The three options are 3 pointer, midrange or layup.')

        if (PlayerOneScore >= 11):
            print('Player One Wins!')
            break
        if (PlayerTwoScore >= 11):
            print('Player Two Wins!')
            break

OnePossesion()

'''
1. Player One Starts with the Ball
2. He chooses whether to shoot a 3 pointer, Midrange, or take a layup. (Rolls Shot)
3. Player Two, (the defender) then chooses whether he wants to try and block or not.
    1. If he wants to block, the program rolls the block
        1. Compares if Block is more than Shot = Player Got Blocked
            1. If player gets blocked (a lot higher) defender gets ball. Restart (Back to step 1).
            2. If player gets blocked (only a little), both defenders try and get the rebound
                1. If shooter gets ball back, he keeps ball. Restart (Back to step 1).
                2. If defender gets ball, he becomes the shooter. Restart (Back to step 1).
        2. Compares if Shot is enough to make the bucket (Player Shot is higher than block).
            3 Pointer:
                1. If higher than 28, he makes the shot. 
                    1. Adds points to player who made shot. Restart (Back to step 1).
                2. If lower than 28 but higher than 14, he hits the rim. Both players try to rebound.
                    1. If shooter gets ball back, he keeps ball. Restart (Back to step 1).
                    2. If defender gets ball, he becomes the shooter. Restart (Back to step 1).
                3. If lower than 14, he misses the rim entirely. Defender gets ball. Restart (Back to step 1)
    2. If he doesn't want to block
        1. If higher than 28, he makes the shot. 
             1. Adds points to player who made shot. Restart (Back to step 1).
        2. If lower than 28 you missed. Player Two gets ball. Restart (Back to step 1).
'''

