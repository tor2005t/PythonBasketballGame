import Tkinter
import tkMessageBox
import random

top = Tkinter.Tk()

def ShootThreePointer():
    ShotRoll = random.randrange(1,30)
    tkMessageBox.showinfo('Shoot Three Pointer', 'Three Point Roll: ' + str(ShotRoll))

def ShootMidrange():
    ShotRoll = random.randrange(1,30)
    tkMessageBox.showinfo('Shoot Midrange Shot', 'Midrange Roll: ' + str(ShotRoll))

def ShootLayup():
    ShotRoll = random.randrange(1,30)
    tkMessageBox.showinfo('Shoot Layup', 'Layup Roll: ' + str(ShotRoll))

def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
C = Tkinter.Button(top, text ='Shoot Three Pointer', command = ShootThreePointer)
D = Tkinter.Button(top, text ='Shoot Midrange Shot', command = ShootMidrange)
E = Tkinter.Button(top, text ='Shoot Layup', command = ShootLayup)

C.pack()
D.pack()
E.pack()
top.mainloop()