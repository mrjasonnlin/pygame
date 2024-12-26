import time
import keyboard
import pyfirmata

# set up arduino board
board = pyfirmata.Arduino('COM4')

# start while loop to keep blinking indefinitely
while True:

    if keyboard.is_pressed('esc'): # stop making the arduino blink if the escape key is pressed
        break

    board.digital[13].write(1) # turn pin 13 ON
    time.sleep(0.5)            # wait 1/2 second
    board.digital[13].write(0) # turn pin 13 OFF
    time.sleep(0.5)            # wait 1/2 second