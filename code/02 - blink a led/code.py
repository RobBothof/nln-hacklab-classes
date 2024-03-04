# import libraries 
import board
import digitalio
import time

# Configure to use pin GP25 as an output.
led = digitalio.DigitalInOut(board.GP25)
led.direction=digitalio.Direction.OUTPUT

# Loop forever.
while True:
     # Turn the buildin LED on
     led.value=1
     # Pause for 2 seconds
     time.sleep(2)
     # Turn the buildin LED off
     led.value=0
     # Pause for 3 seconds
     time.sleep(3)