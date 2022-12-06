# Uvozi knjižnice
from sense_hat import SenseHat
from time import sleep

# Nastavi Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavi barvni senzor
sense.color.gain = 60 # Nastavi občutljivost senzorja
sense.color.integration_cycles = 64 # Interval, v katerem bo opravljeno branje

# Doda barvne spremenljivke in sliko

# Prikaže sliko












