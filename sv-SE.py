# Importera biblioteken
from sense_hat import SenseHat
from time import sleep

# Ställ in Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Ställ in färgsensorn
sense.color.gain = 60 # Ställ in sensorns känslighet
sense.color.integration_cycles = 64 # Intervallet med vilket avläsningen kommer att ske

# Lägg till färgvariabler och bild

# Visa bilden













