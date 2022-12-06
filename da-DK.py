# Importér bibliotekerne
from sense_hat import SenseHat
from time import sleep

# Konfigurer Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Konfigurer farvesensoren
sense.color.gain = 60 # Indstil sensorens følsomhed
sense.color.integration_cycles = 64 # Intervallet, som aflæsningen vil blive taget med

# Tilføj farvevariabler og billede

# Vis billedet












