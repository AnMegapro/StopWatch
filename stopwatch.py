from tkinter import *
from random import randint as rnd
from time import time

timeOld=time()
window = Tk()
window.geometry("500x550")
Game=True
startP=0.0
first=True
def UpTime():
    timeL["text"]=str(int((time()-timeOld)//1)//60)+":"+str(int((time()-timeOld)//1)%60)+":"+str(int(((time()-timeOld)//0.001)%1000))
    if Game:
        window.after(100, UpTime)

def StartT():
    global StTime
    global Game
    global startP
    global timeOld
    global first
    if first:
        print("New")
        startP=time()
        timeOld=time()
    if Game==False and first==False:
        timeOld+=-startP+time()
    first=False
    Game=True
    UpTime()

def Stop():
    global Game
    global startP
    global first
    Game=False
    startP=time()
    first=False

def Clear():
    global Game
    global timeOld
    global first

    Game=False
    first=True
    timeL["text"]="00:00.00"
    
name=Label(window, text="Stopwatch")
timeL=Label(window, text="00:00:00")
Bstart=Button(window,text="Start", command =StartT)
Bstop=Button(window,text="Stop", command =Stop)
BClear=Button(window,text="Clear", command =Clear)
name.config(font=("Courier", 30))
timeL.config(font=("Courier", 20))
Bstart.config(font=("Courier", 20))
Bstop.config(font=("Courier", 20))
BClear.config(font=("Courier", 20))
   
name.pack()
timeL.pack()
Bstart.place(x=200,y=100,width=100,height=100)
Bstop.place(x=300,y=100,width=100,height=100)
BClear.place(x=100,y=100,width=100,height=100)

window.mainloop()
