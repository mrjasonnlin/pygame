# This code is supporting material for the book
# Python Programming for Arduino
# by Pratik Desai
# published by PACKT Publishing

# Define the action associated with Start button press
def onStartButtonPress():
    redPin.write(redVar.get())
    greenPin.write(greenVar.get())

# Define the action associated with Stop button press
def onStopButtonPress():
    redPin.write(0)
    greenPin.write(0)

import       tkinter
import pyfirmata
from time import sleep

# Associate port and board with pyFirmata
port = 'com4'
board = pyfirmata.Arduino(port)
sleep(5)

# Define pins 
redPin = board.get_pin('d:12:o')
greenPin = board.get_pin('d:4:o')

# Initialize main windows with title and size
top =       tkinter.Tk()
top.title("Checkbox example")

# Create Checkbox for Red LED
redVar =       tkinter.IntVar()
redCheckBox =       tkinter.Checkbutton(top,
                                  text="Red LED",
                                  variable=redVar)
redCheckBox.grid(column=1, row=1)

# Create Checkbox for Green LED
greenVar =       tkinter.IntVar()
greenCheckBox =       tkinter.Checkbutton(top,
                                    text="Green LED",
                                    variable=greenVar)
greenCheckBox.grid(column=2, row=1)

# Create Start button and associate with onStartButtonPress method
StartButton =       tkinter.Button(top,
                             text="Start",
                             command=onStartButtonPress)
StartButton.grid(column=1, row=2)

# Create Stop button and associate with onStopButtonPress method
stopButton =       tkinter.Button(top,
                            text="Stop",
                            command=onStopButtonPress)
stopButton.grid(column=2, row=2)

# Create Exit button and destroy the window
exitButton =       tkinter.Button(top,
                            text="Exit",
                            command=top.quit)
exitButton.grid(column=3, row=2)

# Start and open the window
top.mainloop()