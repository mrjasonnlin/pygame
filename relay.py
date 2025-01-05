import pyfirmata
from time import sleep

port = 'com5'
board = pyfirmata.Arduino(port)
sleep(7)
ledPin4 = board.get_pin('d:12:o')  # blue ,tie in 5v gnd


def setFord():
    t = 0.2
    ledPin4.write(1)
    sleep(t)
    ledPin4.write(0)
    sleep(t)


def setBack():
    t = 0.4
    ledPin4.write(1)
    sleep(t)
    ledPin4.write(0)
    sleep(t)


while True:

    # Continue or break the testing process
    i = input("Enter 'y' to forward+back or ,'f' to forward or 'b' to back ,Enter to quit): ")
    if i == 'y':
        for y in range(0, 10, 1):
            setFord()
            setBack()
    elif i == 'f':
        for f in range(0, 10, 1):
            setFord()

    elif i == 'b':
        for b in range(0, 10, 1):
            setBack()

    else:
        board.exit()
        break