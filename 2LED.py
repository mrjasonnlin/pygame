import tkinter as tk
import pyfirmata
from pyfirmata import SERVO
from time import sleep

port = 'com4'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:12:o')
servopin = 13
board.digital[servopin].mode = SERVO

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

def setServoAngle(servopin, angle):
    board.digital[servopin].write(angle)
    sleep(0.015)


def servoFord():
    for y in range(0, 3, 1):
        for i in range(0, 180):
            setServoAngle(servopin, i)
        for i in range(180, 1, -1):
            setServoAngle(servopin, i)


def servoBack():
    for y in range(0, 3, 1):
        for i in range(0, 90):
            setServoAngle(servopin, i)
        for i in range(90, 1, -1):
            setServoAngle(servopin, i)

def servoFordBack():
    servoFord()
    servoBack()


startButton = tk.Button(top, text="LED燈亮10秒", command=onStartButtonPress10)
startButton.pack()

startButton2 = tk.Button(top, text="LED燈亮30秒", command=onStartButtonPress30)
startButton2.pack()

startButton3 = tk.Button(top, text="LED燈慢閃爍10次", command=setFord)
startButton3.pack()

startButton4 = tk.Button(top, text="LED燈快閃爍10次", command=setBack)
startButton4.pack()

startButton5 = tk.Button(top, text="LED燈快慢閃爍10次", command=setFordBack)
startButton5.pack()

startButton6 = tk.Button(top, text="伺服馬達180度來回3次", command=servoFord)
startButton6.pack()

startButton7 = tk.Button(top, text="伺服馬達90度來回3次", command=servoBack)
startButton7.pack()

startButton8 = tk.Button(top, text="伺服馬達180+90度來回3次", command=servoFordBack)
startButton8.pack()

top.mainloop()
