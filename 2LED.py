import tkinter as tk
import pyfirmata
from time import sleep
port = 'com4'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:12:o')

top = tk.Tk()
top.title("blink led using button")
top.minsize(300,30)

def onStartButtonPress():
    startButton.config(state=tk.DISABLED)
    ledPin.write(1)
    sleep(5)
    ledPin.write(0)
    startButton.config(state=tk.ACTIVE)

startButton = tk.Button(top, text = "start", command=onStartButtonPress)
startButton.pack()



top.mainloop()