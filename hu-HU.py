# Programkönyvtárak importálása
from sense_hat import SenseHat
from time import sleep

# Sense HAT beállítása
sense = SenseHat()
sense.set_rotation(270)

# Színérzékelő beállítása
sense.color.gain = 60 # Az érzékelő érzékenységének beállítása
sense.color.integration_cycles = 64 # Az egyes leolvasások között eltelt idő

# Színváltozók és kép hozzáadása

# Kép megjelenítése













