# Importeer de bibliotheken
from sense_hat import SenseHat
from time import sleep

# Stel de Sense HAT in
sense = SenseHat()
sense.set_rotation(270)

# Stel kleurensensor in
sense.color.gain = 60 # Stel de gevoeligheid van de sensor in
sense.color.integration_cycles = 64 # Het interval waarmee de meting wordt uitgevoerd

# Kleurvariabelen en afbeelding toevoegen

# Geef de afbeelding weer 












