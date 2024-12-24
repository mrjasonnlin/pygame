from pyfirmata import Arduino
from pyfirmata import SERVO
from time import sleep

# Setting up the Arduino board
port = 'COM4'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

# Set mode of the pin 13 as SERVO
pin = 13
board.digital[pin].mode = SERVO


# Custom angle to set Servo motor angle
def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)


def setFord():
    for i in range(0, 180):
        setServoAngle(pin, i)
    for i in range(180, 1, -1):
        setServoAngle(pin, i)


def setBack():
    for i in range(0, 90):
        setServoAngle(pin, i)
    for i in range(90, 1, -1):
        setServoAngle(pin, i)


# Testing the function by rotating motor in both direction
while True:

    # Continue or break the testing process
    i = input("Enter 'y' to forward+back or ,'f' to forward or 'b' to back ,Enter to quit):  ")
    if i == 'y':
        for y in range(0, 3, 1):
            setFord()
            setBack()
    elif i == 'f':
        for y in range(0, 3, 1):
            setFord()
    elif i == 'b':
        for y in range(0, 3, 1):
            setBack()
    else:
        board.exit()
        break