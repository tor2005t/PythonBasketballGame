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

a = Location()
a.CreateGraphic()
a.Move('left')
a.CreateGraphic()
a.Move('forward')
a.CreateGraphic()