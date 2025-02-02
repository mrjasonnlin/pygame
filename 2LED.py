import tkinter as tk
from pyfirmata import Arduino, util
import pyfirmata
from pyfirmata import SERVO
from time import sleep

port = 'com4'
board = Arduino(port)  # pyfirmata.
sleep(5)
ledPin = board.get_pin('d:12:o')
beepPin = board.get_pin('d:3:o')
bigPin = board.get_pin('d:5:o')
pushPin = board.get_pin('d:6:o')
dataPin = board.get_pin('d:7:o')
ledPin8 = board.get_pin('d:8:o')  # blue ,tie in 5v gnd
ledPin9 = board.get_pin('d:9:o')  # green
ledPin10 = board.get_pin('d:10:o')  # white
ledPin11 = board.get_pin('d:11:o')  # orange
servopin = 13
board.digital[servopin].mode = SERVO
t = 10
temp = pyfirmata.util.Iterator(board)
temp.start()


top = tk.Tk()
top.title("Jason的ARDUINO實驗板")
top.minsize(200, 300)
top.resizable(True, True)
top.configure(background='#89CFF0')


def beep():
    for y in range(1, 3, 1):
        beepPin.write(1)
        sleep(y)
        beepPin.write(0)
        sleep(1)


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
    for y in range(1, 10, 1):
        ledPin.write(1)
        sleep(0.2)
        ledPin.write(0)
        sleep(0.2)

        ledPin.write(1)
        sleep(0.4)
        ledPin.write(0)
        sleep(0.4)

        beepPin.write(1)
        sleep(1)
        beepPin.write(0)
        sleep(1)

def setServoAngle(servopin, angle):
    board.digital[servopin].write(angle)
    sleep(0.015)


def servoFord():
    for y in range(0, 3, 1):
        for i in range(0, 180, 3):
            setServoAngle(servopin, i)
        for i in range(180, 0, -3):
            setServoAngle(servopin, i)
    beep()


def servoBack():
    for y in range(0, 3, 1):
        for i in range(0, 90, 3):
            setServoAngle(servopin, i)
        for i in range(90, 0, -3):
            setServoAngle(servopin, i)
    beep()

def servoFordBack():
    servoFord()
    servoBack()


notime = 0.6

def N1():
    # 1
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # comma
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)


def N2():
    # 2
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # comma
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)


def N3():
    # 3
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)

def N4():
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)

def N5():
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)

def N6():
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)

def N7():
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)

def N8():
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)

def N9():
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)

def N0():
    bigPin.write(0)

    pushPin.write(0)
    dataPin.write(0)  # .
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(1)  # c2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # L2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C3
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R2
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # R1
    pushPin.write(1)

    pushPin.write(0)
    dataPin.write(0)  # C1
    pushPin.write(1)

    bigPin.write(1)
    sleep(notime)


def runno():
    for y in range(0, 3, 1):
        N1()
        N2()
        N3()
        N4()
        N5()
        N6()
        N7()
        N8()
        N9()
        N0()
        beep()

def stepFord():
    sft = 0.01
    for a in range(0, 4, 1):
        for f in range(0, 20, 1):
            ledPin8.write(1)
            sleep(sft)
            ledPin8.write(0)

            ledPin11.write(1)
            sleep(sft)
            ledPin11.write(0)

            ledPin9.write(1)
            sleep(sft)
            ledPin9.write(0)

            ledPin10.write(1)
            sleep(sft)
            ledPin10.write(0)
    beep()


def stepBack():
    sbt = 0.01
    for a in range(0, 4, 1):
        for b in range(0, 20, 1):
            ledPin10.write(1)
            sleep(sbt)
            ledPin10.write(0)
            ledPin9.write(1)
            sleep(sbt)
            ledPin9.write(0)
            ledPin11.write(1)
            sleep(sbt)
            ledPin11.write(0)
            ledPin8.write(1)
            sleep(sbt)
            ledPin8.write(0)
    beep()

def stepRun():
    stepFord()
    stepBack()


mylabel1 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='01', bitmap='info',
                    compound='left')  # bitmap show left
mylabel1.grid(column=3, row=2)
# mylabel1.pack(fill='x')
startButton = tk.Button(top, bd=5, bg='#89CFF0', font=('Arial', 10, 'bold'), text="LED燈亮短",
                        command=onStartButtonPress10)
startButton.grid(column=4, row=2)
# startButton.pack() #pack(fill='x')

mylabel2 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='02', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel2.grid(column=3, row=3)
# mylabel2.pack(fill='x')
startButton2 = tk.Button(top, bd=5, bg='#89CFF0', font=('Arial', 10, 'bold'), text="LED燈亮長",
                         command=onStartButtonPress20)
startButton2.grid(column=4, row=3)
# startButton2.pack() #pack(fill='x')

mylabel3 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='03', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel3.grid(column=3, row=4)
# mylabel3.pack(fill='x')
startButton3 = tk.Button(top, bd=5, bg='#89CFF0', font=('Arial', 10, 'bold'), text="LED燈每次2秒閃爍10次",
                         command=setBlinkslow)
startButton3.grid(column=4, row=4)
# startButton3.pack() #pack(fill='x')

mylabel4 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='04', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel4.grid(column=3, row=5)
# mylabel4.pack(fill='x')
startButton4 = tk.Button(top, bd=5, bg='#89CFF0', font=('Arial', 10, 'bold'), text="LED燈每次1秒閃爍10次",
                         command=setBlinkfast)
startButton4.grid(column=4, row=5)
# startButton4.pack() #pack(fill='x')

mylabel5 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='05', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel5.grid(column=3, row=6)
# mylabel5.pack(fill='x')
startButton5 = tk.Button(top, bd=5, bg='#89CFF0', font=('Arial', 10, 'bold'), text="LED燈快慢閃爍10次", command=setBlinkfs)
startButton5.grid(column=4, row=6)
# startButton5.pack() #pack(fill='x')

mylabel6 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='06', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel6.grid(column=3, row=7)
# mylabel6.pack(fill='x')
startButton6 = tk.Button(top, bd=5, bg='#FF7F7F', font=('Arial', 10, 'bold'), text="伺服馬達180度來回3次", command=servoFord)
startButton6.grid(column=4, row=7)
# startButton6.pack() #pack(fill='x')

mylabel7 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='07', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel7.grid(column=3, row=8)
# mylabel8.pack(fill='x')
startButton7 = tk.Button(top, bd=5, bg='#FF7F7F', font=('Arial', 10, 'bold'), text="伺服馬達90度來回3次", command=servoBack)
startButton7.grid(column=4, row=8)
# startButton7.pack() #pack(fill='x')

mylabel8 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='08', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel8.grid(column=3, row=9)
# mylabel8.pack(fill='x')
startButton8 = tk.Button(top, bd=5, bg='#FF7F7F', font=('Arial', 10, 'bold'), text="伺服馬達180+90度來回3次",
                         command=servoFordBack)
startButton8.grid(column=4, row=9)
# startButton8.pack() #pack(fill='x')

mylabel9 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='09', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel9.grid(column=3, row=10)
# mylabel9.pack(fill='x')
startButton9 = tk.Button(top, bd=5, bg='#FF7F7F', font=('Arial', 10, 'bold'), text="蜂鳴器", command=beep)
startButton9.grid(column=4, row=10)
# startButton9.pack() #pack(fill='x')

mylabel10 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='10', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel10.grid(column=3, row=11)
startButton9 = tk.Button(top, bd=5, bg='#FF7F7F', font=('Arial', 10, 'bold'), text="74HC595", command=runno)
startButton9.grid(column=4, row=11)

mylabel11 = tk.Label(top, bd=5, fg='#000', bg='#fbfafe', font=('Arial', 10, 'bold'), text='11', bitmap='info',
                    compound='left')  # 建立 label 標籤
mylabel11.grid(column=3, row=12)
startButton11 = tk.Button(top, bd=5, bg='#FF7F7F', font=('Arial', 10, 'bold'), text="步進馬達", command=stepRun)
startButton11.grid(column=4, row=12)

top.mainloop()
