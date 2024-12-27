import tkinter as tk
import pyfirmata
from time import sleep

port = 'com4'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:12:o')

top = tk.Tk()
top.title("blink led using button")
top.minsize(300, 300)


def onStartButtonPress10():
    startButton.config(state=tk.DISABLED)
    ledPin.write(1)
    sleep(10)
    ledPin.write(0)
    startButton.config(state=tk.ACTIVE)

def onStartButtonPress30():
    startButton.config(state=tk.DISABLED)
    ledPin.write(1)
    sleep(30)
    ledPin.write(0)
    startButton.config(state=tk.ACTIVE)

def setFord():
    for y in range(0, 10, 1):
        t = 2
        ledPin.write(1)
        sleep(t)
        ledPin.write(0)
        sleep(t)
def setBack():
    for y in range(0, 10, 1):
        t = 0.4
        ledPin.write(1)
        sleep(t)
        ledPin.write(0)
        sleep(t)

def setFordBack():
    for y in range(0, 10, 1):
        t = 0.2
        ledPin.write(1)
        sleep(t)
        ledPin.write(0)
        sleep(t)
        t = 0.4
        ledPin.write(1)
        sleep(t)
        ledPin.write(0)
        sleep(t)

startButton = tk.Button(top, text="亮10秒", command=onStartButtonPress10)
startButton.pack()

startButton2 = tk.Button(top, text="亮30秒", command=onStartButtonPress30)
startButton2.pack()

startButton3 = tk.Button(top, text="慢閃爍10次", command=setFord)
startButton3.pack()

startButton4 = tk.Button(top, text="快閃爍10次", command=setBack)
startButton4.pack()

startButton5 = tk.Button(top, text="快慢閃爍10次", command=setFordBack)
startButton5.pack()
top.mainloop()
