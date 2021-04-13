import Tkinter
import tkMessageBox
import random

top = Tkinter.Tk()

class Player():
    def __init__(self,name):
        self.name = name
        self.ThreePoint = 0
        self.Midrange = 0
        self.Layup = 0
        self.Roll = 0

    def ShootThreePointer(self):
        self.Roll = random.randrange(1,30) + self.ThreePoint
        tkMessageBox.showinfo('Shoot Three Pointer', 'Three Point Roll: ' + str(self.Roll))

    def ShootMidrange(self):
        self.Roll = random.randrange(1,30) + self.Midrange
        tkMessageBox.showinfo('Shoot Midrange Shot', 'Midrange Roll: ' + str(self.Roll))

    def ShootLayup(self):
        self.Roll = random.randrange(1,30) + self.Layup
        tkMessageBox.showinfo('Shoot Layup', 'Layup Roll: ' + str(self.Roll))

def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
p = Player("Micheal")
B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
C = Tkinter.Button(top, text ='Shoot Three Pointer', command = p.ShootThreePointer)
D = Tkinter.Button(top, text ='Shoot Midrange Shot', command = p.ShootMidrange)
E = Tkinter.Button(top, text ='Shoot Layup', command = p.ShootLayup)

C.pack()
D.pack()
E.pack()
top.mainloop()

#Fix Values not being added (not sure whats wrong)