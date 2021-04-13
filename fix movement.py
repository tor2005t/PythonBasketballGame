class Court1v1():
    def __init__(self):
        self.PlayerOnePossession = True
        self.PlayerTwoPossession = False

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

a = Court1v1()
a.CreateGraphic()
a.Move('right')
a.CreateGraphic()
a.Move('forward')
a.CreateGraphic()
a.Move('left')
a.CreateGraphic()