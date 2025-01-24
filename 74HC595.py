import pyfirmata
from time import sleep
port = 'com4'
board = pyfirmata.Arduino(port)
bigPin = board.get_pin('d:5:o')
pushPin = board.get_pin('d:6:o')
dataPin = board.get_pin('d:7:o')

# 1
bigPin.write(0)

pushPin.write(0)
dataPin.write(0) # comma
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # c2
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # L1
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # L2
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # C3
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # R2
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # R1
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # C1
pushPin.write(1)

bigPin.write(1)
sleep(1)

#2
bigPin.write(0)

pushPin.write(0)
dataPin.write(0) # comma
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # c2
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # L1
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # L2
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # C3
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # R2
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # R1
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # C1
pushPin.write(1)

bigPin.write(1)
sleep(1)

#3
bigPin.write(0)

pushPin.write(0)
dataPin.write(0) # .
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # c2
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # L1
pushPin.write(1)

pushPin.write(0)
dataPin.write(1) # L2
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # C3
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # R2
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # R1
pushPin.write(1)

pushPin.write(0)
dataPin.write(0) # C1
pushPin.write(1)

bigPin.write(1)
sleep(1)

board.exit()