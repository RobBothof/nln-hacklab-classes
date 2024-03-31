
# import libraries 
import board
import digitalio
import analogio
import time
import usb_midi
import adafruit_midi
import math

# import auxiliar libraries
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

# Configure to use pin GP15 as a digital input.
button1 = digitalio.DigitalInOut(board.GP15)
button1.direction=digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
button1_previous = button1.value

# The adc pins are configured by default as analog inputs.
pot1 = analogio.AnalogIn(board.GP26)
pot1_previous = 0

# Configure Midi
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0, midi_out=usb_midi.ports[1], out_channel=0)

# Loop forever.
while True:   
    # Read the button and potentiometer values
    button1_current = button1.value
    pot1_current = math.floor(pot1.value / 512)

    # If the button has changed
    if button1_current != button1_previous:

        if button1_current == 0:
            # Button 1 pressed
            # Send a note ON with maximum velocity
            midi.send(NoteOn(60, 127))

        if button1_current == 1:
            # Button 1 released
            # Send a note OFF with maximum velocity
            midi.send(NoteOff(60, 0))

        # Update the previous value
        button1_previous = button1_current

    # If the potentiometer has changed
    if pot1_current != pot1_previous:
        # Send a control change with the potentiometer value
        midi.send(ControlChange(1, pot1_current))

        # Update the previous value
        pot1_previous = pot1_current

    # Pause for 1/100th of a second
    time.sleep(0.01)

