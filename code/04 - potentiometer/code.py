# import libraries 
import board
import analogio
import time

# The adc pins are configured by default as analog inputs.
adc0 = analogio.AnalogIn(board.GP26)

# Loop forever.
while True:
    # Read and print the value of the potentiometer
    print(adc0.value)

    # Pause for 1/100th of a second
    time.sleep(0.01)
