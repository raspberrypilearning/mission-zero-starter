# Importujte knižnice
from sense_hat import SenseHat
from time import sleep

# Nastavte Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Nastavte snímač farieb
sense.color.gain = 60 # Nastavte citlivosť snímača
sense.color.integration_cycles = 64 # Interval, v ktorom sa bude realizovať snímanie

# Pridajte farebné premenné a obrázok

# Zobrazte obrázok










