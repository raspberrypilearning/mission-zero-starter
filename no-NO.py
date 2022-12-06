# Importer bibliotekene
from sense_hat import SenseHat
from time import sleep

# Sett opp Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Sett opp fargesensoren
sense.color.gain = 60 # Angi følsomheten til sensoren
sense.color.integration_cycles = 64 # Intervallet hvor avlesningen vil ta

# Legg til fargevariabler og bilde

# Vis bildet 












