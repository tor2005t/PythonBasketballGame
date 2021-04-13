#Keeps Track of Player's Position on the Court
'''
[A1][A2][A3][A4][A5]
[B1][B2][B3][B4][B5]
[C1][C2][C3][C4][C5]
[D1][D2][D3][D4][D5]
[E1][E2][E3][E4][E5]
'''
'''
#Player One Locations
P1Location = {'P1A1': False, 'P1A2': False,'P1A3': False,'P1A4': False,'P1A5': False,
              'P1B1': False, 'P1B2': False,'P1B3': False,'P1B4': False,'P1B5': False,
              'P1C1': False, 'P1C2': False,'P1C3': False,'P1C4': False,'P1C5': False,
              'P1D1': False, 'P1D2': False,'P1D3': False,'P1D4': False,'P1D5': False,
              'P1E1': False, 'P1E2': False,'P1E3': True,'P1E4': False,'P1E5': False,
              }

#Player Two Locations
P2Location = {'P2A1': False, 'P2A2': False,'P2A3': False,'P2A4': False,'P2A5': False,
              'P2B1': False, 'P2B2': False,'P2B3': False,'P2B4': False,'P2B5': False,
              'P2C1': False, 'P2C2': False,'P2C3': False,'P2C4': False,'P2C5': False,
              'P2D1': False, 'P2D2': False,'P2D3': False,'P2D4': False,'P2D5': False,
              'P2E1': False, 'P2E2': False,'P2E3': True,'P2E4': False,'P2E5': False,
              }
'''
'''
[1,5][2,5][3,5][4,5][5,5]
[1,4][2,4][3,4][4,4][5,4]
[1,3][2,3][3,3][4,3][5,3]
[1,2][2,2][3,2][4,2][5,2]
[1,1][2,1][3,1][4,1][5,1]
'''

#Court Graphics
OneOne = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[x][ ][ ][ ][ ]'
TwoOne = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][x][ ][ ][ ]'
ThreeOne = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][x][ ][ ]'
FourOne = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][x][ ]'
FiveOne = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][x]'

OneTwo = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[x][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
TwoTwo = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][x][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
ThreeTwo = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][x][ ][ ]\n[ ][ ][ ][ ][ ]'
FourTwo = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][x][ ]\n[ ][ ][ ][ ][ ]'
FiveTwo = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][x]\n[ ][ ][ ][ ][ ]'

OneThree = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[x][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
TwoThree = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][x][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
ThreeThree = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][x][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
FourThree = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][x][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
FiveThree = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][x]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'

OneFour = '[ ][ ][ ][ ][ ]\n[x][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
TwoFour = '[ ][ ][ ][ ][ ]\n[ ][x][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
ThreeFour = '[ ][ ][ ][ ][ ]\n[ ][ ][x][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
FourFour = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][x][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
FiveFour = '[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][x]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'

OneFive = '[x][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
TwoFive = '[ ][x][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
ThreeFive = '[ ][ ][x][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
FourFive = '[ ][ ][ ][x][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'
FiveFive = '[ ][ ][ ][ ][x]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]\n[ ][ ][ ][ ][ ]'

#Player One Locations (X,Y Coordinate)
PlayerOneLocation = {'x': 3, 'y': 1}

print('Current Location:')
print(ThreeOne)
while (1 == 1):
    MoveOrShootAction = raw_input('What would you like to do? Shoot, move Forward, Backward, Left or Right? ')
    if (MoveOrShootAction == 'Shoot'):
        print('Shoot!')
    if ((MoveOrShootAction == 'Forward') and (PlayerOneLocation['y'] < 5)):
        print('You moved forward!')
        PlayerOneLocation['y'] = PlayerOneLocation['y'] + 1
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 1)):
            print(OneOne)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 2)):
            print(OneTwo)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 3)):
            print(OneThree)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 4)):
            print(OneFour)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 5)):
            print(OneFive)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 1)):
            print(TwoOne)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 2)):
            print(TwoTwo)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 3)):
            print(TwoThree)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 4)):
            print(TwoFour)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 5)):
            print(TwoFive)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 1)):
            print(ThreeOne)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 2)):
            print(ThreeTwo)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 3)):
            print(ThreeThree)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 4)):
            print(ThreeFour)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 5)):
            print(ThreeFive)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 1)):
            print(FourOne)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 2)):
            print(FourTwo)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 3)):
            print(FourThree)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 4)):
            print(FourFour)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 5)):
            print(FourFive)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 1)):
            print(FiveOne)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 2)):
            print(FiveTwo)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 3)):
            print(FiveThree)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 4)):
            print(FiveFour)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 5)):
            print(FiveFive)
    elif ((MoveOrShootAction == 'Forward') and (PlayerOneLocation == 5)):
        print('You cannot move forward!')
    if ((MoveOrShootAction == 'Backward') and (PlayerOneLocation['y'] > 1)):
        print('You moved backwards!')
        PlayerOneLocation['y'] = PlayerOneLocation['y'] - 1
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 1)):
            print(OneOne)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 2)):
            print(OneTwo)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 3)):
            print(OneThree)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 4)):
            print(OneFour)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 5)):
            print(OneFive)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 1)):
            print(TwoOne)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 2)):
            print(TwoTwo)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 3)):
            print(TwoThree)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 4)):
            print(TwoFour)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 5)):
            print(TwoFive)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 1)):
            print(ThreeOne)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 2)):
            print(ThreeTwo)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 3)):
            print(ThreeThree)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 4)):
            print(ThreeFour)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 5)):
            print(ThreeFive)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 1)):
            print(FourOne)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 2)):
            print(FourTwo)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 3)):
            print(FourThree)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 4)):
            print(FourFour)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 5)):
            print(FourFive)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 1)):
            print(FiveOne)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 2)):
            print(FiveTwo)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 3)):
            print(FiveThree)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 4)):
            print(FiveFour)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 5)):
            print(FiveFive)
    elif ((MoveOrShootAction == 'Backwards') and (PlayerOneLocation['y'] == 1)):
        print('You cannot move backwards!')

    if ((MoveOrShootAction == 'Right') and (PlayerOneLocation['x'] < 5)):
        print('You moved right!')
        PlayerOneLocation['x'] = PlayerOneLocation['x'] + 1
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 1)):
            print(OneOne)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 2)):
            print(OneTwo)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 3)):
            print(OneThree)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 4)):
            print(OneFour)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 5)):
            print(OneFive)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 1)):
            print(TwoOne)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 2)):
            print(TwoTwo)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 3)):
            print(TwoThree)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 4)):
            print(TwoFour)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 5)):
            print(TwoFive)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 1)):
            print(ThreeOne)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 2)):
            print(ThreeTwo)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 3)):
            print(ThreeThree)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 4)):
            print(ThreeFour)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 5)):
            print(ThreeFive)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 1)):
            print(FourOne)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 2)):
            print(FourTwo)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 3)):
            print(FourThree)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 4)):
            print(FourFour)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 5)):
            print(FourFive)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 1)):
            print(FiveOne)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 2)):
            print(FiveTwo)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 3)):
            print(FiveThree)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 4)):
            print(FiveFour)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 5)):
            print(FiveFive)
    elif ((MoveOrShootAction == 'Right') and (PlayerOneLocation['x'] == 5)):
        print('You cannot move right!')

    if ((MoveOrShootAction == 'Left') and (PlayerOneLocation['x'] > 1)):
        print('You moved left!')
        PlayerOneLocation['x'] = PlayerOneLocation['x'] - 1
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 1)):
            print(OneOne)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 2)):
            print(OneTwo)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 3)):
            print(OneThree)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 4)):
            print(OneFour)
        if ((PlayerOneLocation['x'] == 1) and (PlayerOneLocation['y'] == 5)):
            print(OneFive)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 1)):
            print(TwoOne)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 2)):
            print(TwoTwo)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 3)):
            print(TwoThree)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 4)):
            print(TwoFour)
        if ((PlayerOneLocation['x'] == 2) and (PlayerOneLocation['y'] == 5)):
            print(TwoFive)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 1)):
            print(ThreeOne)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 2)):
            print(ThreeTwo)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 3)):
            print(ThreeThree)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 4)):
            print(ThreeFour)
        if ((PlayerOneLocation['x'] == 3) and (PlayerOneLocation['y'] == 5)):
            print(ThreeFive)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 1)):
            print(FourOne)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 2)):
            print(FourTwo)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 3)):
            print(FourThree)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 4)):
            print(FourFour)
        if ((PlayerOneLocation['x'] == 4) and (PlayerOneLocation['y'] == 5)):
            print(FourFive)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 1)):
            print(FiveOne)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 2)):
            print(FiveTwo)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 3)):
            print(FiveThree)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 4)):
            print(FiveFour)
        if ((PlayerOneLocation['x'] == 5) and (PlayerOneLocation['y'] == 5)):
            print(FiveFive)
    elif ((MoveOrShootAction == 'Left') and (PlayerOneLocation['x'] == 1)):
        print('You cannot move left!')




