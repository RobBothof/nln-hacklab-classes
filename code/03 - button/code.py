# import libraries 
import board
import digitalio
import time

# Configure to use pin GP25 as an output.
led = digitalio.DigitalInOut(board.GP25)
led.direction=digitalio.Direction.OUTPUT

# Configure to use pin GP15 as a digital input.
button = digitalio.DigitalInOut(board.GP15)
button.direction=digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Loop forever.
while True:
     # Set the led to the value of the button
     led.value=button.value
     # Pause for 1/100th of a second
     time.sleep(0.01)