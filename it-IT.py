# Importa le librerie
from sense_hat import SenseHat
from time import sleep

# Imposta il Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Imposta il sensore di colore
sense.color.gain = 60 # Imposta la sensibilità del sensore
sense.color.integration_cycles = 64 # L'intervallo con cui verrà eseguita la lettura

# Aggiungi variabili per il colore e immagine

# Mostra l'immagine












