import pyfirmata
from time import sleep
port = 'com4'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:12:o')

ledPin.write(1)
sleep(50)
ledPin.write(0)

board.exit()