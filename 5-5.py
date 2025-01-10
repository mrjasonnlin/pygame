# This code is supporting material for the book
# Python Programming for Arduino
# by Pratik Desai
# published by PACKT Publishing

# Define the action associated with button press
def onStartButtonPress():
    timePeriod = timePeriodEntry.get()
    timePeriod = float(timePeriod)
    ledBrightness = brightnessScale.get()
    ledBrightness = float(ledBrightness)
    startButton.config(state=DISABLED)
    ledPin.write(ledBrightness / 100.0)
    sleep(timePeriod)
    ledPin.write(0)
    startButton.config(state=ACTIVE)

import   tkinter
from   tkinter import DISABLED, ACTIVE, HORIZONTAL
import pyfirmata
from time import sleep

# Associate port and board with pyFirmata
port = 'com4'
board = pyfirmata.Arduino(port)
sleep(5)
# Define led pins
ledPin = board.get_pin('d:2:p')

# Initialize main windows with title and size
top =   tkinter.Tk()
top.title("Brightness using Scale")

# Text field entry to provide LED on time
timePeriodEntry =   tkinter.Entry(top,
                                bd=5,
                                width=25)
timePeriodEntry.pack()
timePeriodEntry.focus_set()

# Scale to specify LED brightness
brightnessScale =   tkinter.Scale(top,
                                from_=0,
                                to=100,
                                orient=HORIZONTAL)
brightnessScale.pack()

# Create a button on main window and associate it with above method
startButton =   tkinter.Button(top,
                             text="Start",
                             command=onStartButtonPress)
startButton.pack()

# Start and open the window
top.mainloop()