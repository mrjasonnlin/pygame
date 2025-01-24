from pyfirmata import Arduino, util
import pyfirmata
from time import sleep

port = 'com4'

board = Arduino(port) # pyfirmata.

temp = pyfirmata.util.Iterator(board)
temp.start()

sleep(5)
ledPin8 = board.get_pin('d:8:o')  # blue ,tie in 5v gnd
ledPin9 = board.get_pin('d:9:o')  # green
ledPin10 = board.get_pin('d:10:o')  # white
ledPin11 = board.get_pin('d:11:o')  # orange

t = 0.1


def stepFord():
    for a in range(0, 10, 1):
        for f in range(0, 200, 20):
            ledPin8.write(1)
            sleep(t)
            ledPin8.write(0)

            ledPin11.write(1)
            sleep(t)
            ledPin11.write(0)

            ledPin9.write(1)
            sleep(t)
            ledPin9.write(0)

            ledPin10.write(1)
            sleep(t)
            ledPin10.write(0)


def stepBack():
    for a in range(0, 10, 1):
        for b in range(0, 200, 20):
            ledPin10.write(1)
            sleep(t)
            ledPin10.write(0)
            ledPin9.write(1)
            sleep(t)
            ledPin9.write(0)
            ledPin11.write(1)
            sleep(t)
            ledPin11.write(0)
            ledPin8.write(1)
            sleep(t)
            ledPin8.write(0)


while True:

    # Continue or break the testing process
    i = input("Enter 'y' to forward+back or ,'f' to forward or 'b' to back ,Enter to quit): ")
    if i == 'y':
        stepFord()
        stepBack()
    elif i == 'f':
        stepFord()
    elif i == 'b':
        stepBack()
    else:
        board.exit()
        break