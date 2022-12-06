# Bibliotheken importieren
from sense_hat import SenseHat
from time import sleep

# Einrichten des Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Farbsensor einrichten
sense.color.gain = 60 # Empfindlichkeit des Sensors einstellen
sense.color.integration_cycles = 64 # Das Intervall, in dem die Messung durchgeführt wird

# Farbvariablen und Bild hinzufügen

# Das Bild anzeigen 












