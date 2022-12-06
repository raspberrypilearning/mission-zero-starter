# Importer les bibliothèques
from sense_hat import SenseHat
from time import sleep

# Configuer le Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurer le capteur de couleurs
sense.color.gain = 60 # Régler la sensibilité du capteur
sense.color.integration_cycles = 64 # L'intervalle auquel la mesure est effectuée

# Ajouter des variables de couleur et une image

# Afficher l'image













