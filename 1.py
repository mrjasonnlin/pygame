import pyfirmata
from time import sleep
port = 'com3'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:26:o')

ledPin.write(1)
sleep(5)
ledPin.write(0)

board.exit()