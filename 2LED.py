import     tkinter as tk
import pyfirmata
from pyfirmata import SERVO
from time import sleep

port = 'com5'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:12:o')
servopin = 13
board.digital[servopin].mode = SERVO
t = 10

top = tk.Tk()
top.title("blink led using button")
top.minsize(200, 300)
top.resizable(True, True)
top.configure(background='#000')


def onStartButtonPress10():
    startButton.config(state=tk.DISABLED)
    ledPin.write(1)
    sleep(4)
    ledPin.write(0)
    startButton.config(state=tk.ACTIVE)

def onStartButtonPress20():
    startButton.config(state=tk.DISABLED)
    ledPin.write(1)
    sleep(10)
    ledPin.write(0)
    startButton.config(state=tk.ACTIVE)

def setBlinkslow():
    for y in range(0, 10, 1):
        ledPin.write(1)
        sleep(0.8)
        ledPin.write(0)
        sleep(0.8)
def setBlinkfast():
    for y in range(0, 10, 1):
        ledPin.write(1)
        sleep(0.4)
        ledPin.write(0)
        sleep(0.4)

def setBlinkfs():
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

mylabel1 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='1', bitmap='info', compound='left')  # bitmap show left
mylabel1.pack(fill='x')
startButton = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈亮短", command=onStartButtonPress10)
startButton.pack(fill='x')

mylabel2 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='2', bitmap='info', compound='left')  # 建立 label 標籤
mylabel2.pack(fill='x')
startButton2 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈亮長", command=onStartButtonPress20)
startButton2.pack(fill='x')

mylabel3 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='3', bitmap='info', compound='left')  # 建立 label 標籤
mylabel3.pack(fill='x')
startButton3 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈每次2秒閃爍10次", command=setBlinkslow)
startButton3.pack(fill='x')

mylabel4 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='4', bitmap='info', compound='left')  # 建立 label 標籤
mylabel4.pack(fill='x')
startButton4 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈每次1秒閃爍10次", command=setBlinkfast)
startButton4.pack(fill='x')

mylabel5 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='5', bitmap='info', compound='left')  # 建立 label 標籤
mylabel5.pack(fill='x')
startButton5 = tk.Button(top, bd=5, bg='#89CFF0', text="LED燈快慢閃爍10次", command=setBlinkfs)
startButton5.pack(fill='x')

mylabel6 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='6', bitmap='info', compound='left')  # 建立 label 標籤
mylabel6.pack(fill='x')
startButton6 = tk.Button(top, bd=5, bg='#FF7F7F', text="伺服馬達180度來回3次", command=servoFord)
startButton6.pack(fill='x')

mylabel7 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='7', bitmap='info', compound='left')  # 建立 label 標籤
mylabel7.pack(fill='x')
startButton7 = tk.Button(top, bd=5, bg='#FF7F7F',text="伺服馬達90度來回3次", command=servoBack)
startButton7.pack(fill='x')

mylabel8 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial',20,'bold'), text='8', bitmap='info', compound='left')  # 建立 label 標籤
mylabel8.pack(fill='x')
startButton8 = tk.Button(top, bd=5, bg='#FF7F7F',text="伺服馬達180+90度來回3次", command=servoFordBack)
startButton8.pack(fill='x')


top.mainloop()
