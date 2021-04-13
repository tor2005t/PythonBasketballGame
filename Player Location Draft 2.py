'''
LocationP1 = {'OneFive': False, 'TwoFive': False,'ThreeFive': False,'FourFive': False,'FiveFive': False,
              'OneFour': False, 'TwoFour': False,'ThreeFour': False,'FourFour': False,'FiveFour': False,
              'OneThree': False, 'TwoThree': False,'ThreeThree': False,'FourThree': False,'FiveThree': False,
              'OneTwo': False, 'TwoTwo': False,'ThreeTwo': False,'FourTwo': False,'FiveTwo': False,
              'OneOne': False, 'TwoOne': False,'ThreeOne': True,'FourOne': False,'FiveOne': False,
              }
'''

class Location():
    def __init__(self):
        self.Location = {'OneFive': False, 'TwoFive': False,'ThreeFive': False,'FourFive': False,'FiveFive': False,
              'OneFour': False, 'TwoFour': False,'ThreeFour': False,'FourFour': False,'FiveFour': False,
              'OneThree': False, 'TwoThree': False,'ThreeThree': False,'FourThree': False,'FiveThree': False,
              'OneTwo': False, 'TwoTwo': False,'ThreeTwo': False,'FourTwo': False,'FiveTwo': False,
              'OneOne': False, 'TwoOne': False,'ThreeOne': True,'FourOne': False,'FiveOne': False,
                         }
        self.LocationGraphic = []

    def CreateGraphic(self):
        if (self.Location['OneFive'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['TwoFive'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['ThreeFive'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FourFive'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FiveFive'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['OneFour'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['TwoFour'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['ThreeFour'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FourFour'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FiveFour'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['OneThree'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['TwoThree'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['ThreeThree'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FourThree'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FiveThree'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['OneTwo'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['TwoTwo'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['ThreeTwo'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FourTwo'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FiveTwo'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['OneOne'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['TwoOne'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['ThreeOne'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FourOne'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        if (self.Location['FiveOne'] == True):
            self.LocationGraphic.append('[x]')
        else:
            self.LocationGraphic.append('[ ]')
        print(self.LocationGraphic[0] + self.LocationGraphic[1] + self.LocationGraphic[2] + self.LocationGraphic[3] + self.LocationGraphic[4])
        print(self.LocationGraphic[5] + self.LocationGraphic[6] + self.LocationGraphic[7] + self.LocationGraphic[8] + self.LocationGraphic[9])
        print(self.LocationGraphic[10] + self.LocationGraphic[11] + self.LocationGraphic[12] + self.LocationGraphic[13] + self.LocationGraphic[14])
        print(self.LocationGraphic[15] + self.LocationGraphic[16] + self.LocationGraphic[17] + self.LocationGraphic[18] + self.LocationGraphic[19])
        print(self.LocationGraphic[20] + self.LocationGraphic[21] + self.LocationGraphic[22] + self.LocationGraphic[23] + self.LocationGraphic[24])

'''
    def CreateGraphic(self):
        for i in self.Location.keys():
            if (self.Location == ''):
                self.LocationGraphic.append('[ ]')
            else:
                self.LocationGraphic.append('[x]')
        print(self.LocationGraphic)
'''

a = Location()
a.CreateGraphic()
