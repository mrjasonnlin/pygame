import tkinter as tk
import pyfirmata
from pyfirmata import SERVO
from time import sleep

port = 'com5'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:12:o')
servopin = 13
board.digital[servopin].mode = SERVO

top = tk.Tk()
top.title("blink led using button")
top.minsize(200, 300)
top.resizable(True, True)
top.configure(background='#000')


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

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='1', bitmap='info', compound='left')  # bitmap show left
mylabel.pack()
startButton = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈亮10秒", command=onStartButtonPress10)
startButton.pack()

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='2', bitmap='info', compound='left')  # 建立 label 標籤
mylabel.pack()
startButton2 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈亮30秒", command=onStartButtonPress30)
startButton2.pack()

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='3', bitmap='info', compound='left')  # 建立 label 標籤
mylabel.pack()
startButton3 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈慢閃爍10次", command=setFord)
startButton3.pack()

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='4', bitmap='info', compound='left')  # 建立 label 標籤
mylabel.pack()
startButton4 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈快閃爍10次", command=setBack)
startButton4.pack()

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='5', bitmap='info', compound='left')  # 建立 label 標籤
mylabel.pack()
startButton5 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈快慢閃爍10次", command=setFordBack)
startButton5.pack()

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='6', bitmap='info', compound='left')  # 建立 label 標籤
mylabel.pack()
startButton6 = tk.Button(top, bd=5, bg='#FF7F7F', text="伺服馬達180度來回3次", command=servoFord)
startButton6.pack()

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='7', bitmap='info', compound='left')  # 建立 label 標籤
mylabel.pack()
startButton7 = tk.Button(top, bd=5, bg='#FF7F7F',text="伺服馬達90度來回3次", command=servoBack)
startButton7.pack()

mylabel = tk.Label(top, bd=5, fg='#000', bg='#89CFF0', font=('Arial',20,'bold'), text='8', bitmap='info', compound='left')  # 建立 label 標籤
mylabel.pack()
startButton8 = tk.Button(top, bd=5, bg='#FF7F7F',text="伺服馬達180+90度來回3次", command=servoFordBack)
startButton8.pack()

top.mainloop()
