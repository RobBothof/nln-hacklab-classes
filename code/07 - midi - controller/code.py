import digitalio
import analogio
import time
import usb_midi
import adafruit_midi
import math
import board

# Import auxiliar libraries
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

# Configure LED

led1 = digitalio.DigitalInOut(board.GP25)
led1.direction = digitalio.Direction.OUTPUT
led1.value=0

# Configure buttons and potentiometers

# Button 1
button1 = digitalio.DigitalInOut(board.GP15)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
button1_previous = button1.value

# Button 2
button2 = digitalio.DigitalInOut(board.GP14)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP
button2_previous = button2.value

# Potentiometer 1
pot1 = analogio.AnalogIn(board.GP26)
pot1_previous = 0

# Potentiometer 2
pot2 = analogio.AnalogIn(board.GP27)
pot2_previous = 0

# Potentiometer 3
pot3 = analogio.AnalogIn(board.GP28)
pot3_previous = 0

# Configure MIDI
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0)

# Loop forever.
while True:   
    # Read the button and potentiometer values
    button1_current = button1.value
    button2_current = button2.value
    
    pot1_current = math.floor(pot1.value / 512)
    pot2_current = math.floor(pot2.value / 512)
    pot3_current = math.floor(pot3.value / 512)

    # If any button has changed
    if (button1_current != button1_previous) or (button2_current != button2_previous):

        if button1_current == 0:
            # Button 1 pressed
            # Send a note ON with maximum velocity
            midi.send(NoteOn(60, 127))
        elif button1_current == 1:
            # Button 1 released
            # Send a note OFF with maximum velocity
            midi.send(NoteOff(60, 0))

        if button2_current == 0:
            # Button 2 pressed
            # Send a note ON with maximum velocity
            midi.send(NoteOn(61, 127))
        elif button2_current == 1:
            # Button 2 released
            # Send a note OFF with maximum velocity
            midi.send(NoteOff(61, 0))

        # Update the previous values for buttons
        button1_previous = button1_current
        button2_previous = button2_current
        
        # Turn led on to indicate midi is being sent
        led1.value=1

    # If any potentiometer has changed
    if (pot1_current != pot1_previous) or (pot2_current != pot2_previous) or (pot3_current != pot3_previous):
        # Send control changes with the potentiometer values
        midi.send(ControlChange(1, pot1_current))
        midi.send(ControlChange(2, pot2_current))
        midi.send(ControlChange(3, pot3_current))

        # Update the previous values for potentiometers
        pot1_previous = pot1_current
        pot2_previous = pot2_current
        pot3_previous = pot3_current

        # Turn led on to indicate midi is being sent
        led1.value=1

    # Pause for 1/33th of a second
    time.sleep(0.03)
    
    #Turn led off again
    led1.value=0


