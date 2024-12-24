import Tkinter
import pyfirmata
from time import sleep
port = 'com3'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:6:o')

top = Tkinter.Tk()
top.title("blink led using button")
top.minsize(300,30)

def onStartButtonPress():
    startButton.config(state=Tkinter.DISABLED)
    ledPin.write(1)
    sleep(5)
    ledPin.write(0)
    startButton.config(state=Tkinter.ACTIVE)

startButton = Tkinter.Button(top, text = "start", command=onStartButtonPress)
startButton.pack()



top.mainloop()