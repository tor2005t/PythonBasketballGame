import Player
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

    def setSelectShootAction(self,name):
        ShootAction = input('What would you like to do ' + name + '? Shoot a 3 pointer, Midrange shot or Layup? ').lower()
        return ShootAction

    def setBlockAttempt(self,name):
        Blockattempt = input(name + ', Would you like to try to block the shot or go rebound? ').lower()
        return Blockattempt

    def setSelfProgression(self,player_one,player_two):
        self.PlayerOnePossession = player_one
        self.PlayerTwoPossession = player_two

    def printPlayerHasBall(self,player1_name,player2_name):
        if self.PlayerOnePossession == True:
            print(player1_name + ' got the rebound! ' + player2_name + ' has the ball.')
        else:
            print(player2_name + ' got the rebound! ' + player1_name + ' has the ball.')

    def checkWinner(self,player1_name,player2_name):
        if (self.score1 >= 11):
            print(player1_name + ' won!')
        else:
            print(player1_name + ' won!')


    def PlayGame(self):
        while (self.score1 or self.score2 <= 11):#11 = win score
            if (self.PlayerOnePossession == True): #Player1
                ShootAction = Court1v1.setSelectShootAction(Player.name)

            if (self.PlayerTwoPossession == True): #Player2
                ShootAction = Court1v1.setSelectShootAction(Player.name)

            if ((ShootAction == '3 pointer') or (ShootAction == 'midrange') or (ShootAction == 'layup')):
                if (ShootAction == '3 pointer'):
                    if (self.PlayerOnePossession == True):
                        Player.Shoot('3 pointer')
                        ThreePointRoll = Player.Roll__
                    else:
                        Player.Shoot('3 pointer')
                        ThreePointRoll = Player.Roll__

                    if (self.PlayerOnePossession == True):
                       BlockAttempt = Court1v1.setBlockAttempt(Player.name)
                    else:
                        BlockAttempt = Court1v1.setBlockAttempt(Player.name)

                    if (BlockAttempt == 'block'):
                        if (self.PlayerOnePossession == True):
                            Player.Defend('outside block')
                            BlockRoll = Player.Roll__
                        else:
                            Player.Defend('outside block')
                            BlockRoll = Player.Roll__
                        if (ThreePointRoll < BlockRoll - 5):
                            if (self.PlayerOnePossession == True):
                                print(Player.name + ' got fully swatted!')
                                Court1v1.setSelfProgression(False,True)
                                print(Player.name + ' has the Ball!')
                            elif ((self.PlayerTwoPossession == True)):
                                print(Player.name + ' got fully swatted!')
                                Court1v1.setSelfProgression(True,False)
                                print(Player.name + ' has the ball!')
                        if ((ThreePointRoll < BlockRoll) and (ThreePointRoll > BlockRoll - 5)):
                            print('The ball got tipped!')
                            print('You both jump for the rebound!')
                            Player.Defend('rebound')
                            ReboundRollP1 = Player.Roll__
                            Player.Defend('rebound')
                            ReboundRollP2 = Player.Roll__
                            if (ReboundRollP1 > ReboundRollP2):
                                Court1v1.setSelfProgression(True,False)
                                Court1v1.printPlayerHasBall(self,Player.name, Player.name)
                            else:
                                Court1v1.setSelfProgression(False,True)

                        elif ((ThreePointRoll > 28) and (ThreePointRoll > BlockRoll)):
                            if (self.PlayerOnePossession == True):
                                print('Splash! ' + Player.name + '  sank the shot!')
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
                                setSelfProgression(True, False)
                                print(p1.name + ' got the rebound! ' + p1.name + ' has the ball.')
                            else:
                                setSelfProgression(False,True)
                                print(p2.name + ' got the rebound! ' + p2.name + ' has the ball.')
                        elif ((ThreePointRoll < 14) and (ThreePointRoll > BlockRoll)):
                            print('You airballed the shot!')
                            if (self.PlayerOnePossession == True):
                                print(p1.name + ' airballed the shot!')
                                setSelfProgression(False,True)
                                print(p2.name + ' now has the ball.')
                            else:
                                print(p2.name + ' airballed the shot!')
                                setSelfProgression(True,False)
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

            Court1v1.checkWinner(Player.name,Player.name)