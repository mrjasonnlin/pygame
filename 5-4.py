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
    startButton.config(state=   tkinter.DISABLED)
    ledPin.write(ledBrightness / 100.0)
    sleep(timePeriod)
    ledPin.write(0)
    startButton.config(state=   tkinter.ACTIVE)

import    tkinter
import pyfirmata
from time import sleep

# Associate port and board with pyFirmata
port = 'com4'
board = pyfirmata.Arduino(port)
sleep(5)
# Define led pins
ledPin = board.get_pin('d:4:o')

# Initialize main windows with title and size
top =    tkinter.Tk()
top.title("Grid example")

# Text field entry to provide LED on time
timePeriodEntry =    tkinter.Entry(top, bd=5)
timePeriodEntry.grid(column=1, row=1)
timePeriodEntry.focus_set()
  tkinter.Label(top,
              text="Time (seconds)").grid(column=2, row=1)

# Scale to specify LED brightness
brightnessScale =    tkinter.Scale(top,
                                from_=0, to=100,
                                orient=   tkinter.HORIZONTAL)
brightnessScale.grid(column=1, row=2)
  tkinter.Label(top,
              text="Brightness (%)").grid(column=2, row=2)

# Create a button on main window and associate it with above method
startButton =    tkinter.Button(top,
                             text="Start",
                             command=onStartButtonPress)
startButton.grid(column=1, row=3)

# Create Exit button and destroy the window
exitButton =    tkinter.Button(top,
                            text="Exit",
                            command=top.quit)
exitButton.grid(column=2, row=3)

# Start and open the window
top.mainloop()