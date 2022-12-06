# Εισαγωγή βιβλιοθηκών
from sense_hat import SenseHat
from time import sleep

# Ρύθμιση του Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Ρύθμιση του αισθητήρα χρωμάτων
sense.color.gain = 60 # Ρύθμιση της ευαισθησίας του αισθητήρα
sense.color.integration_cycles = 64 # Το μεσοδιάστημα κατά το οποίο θα γίνεται η ανάγνωση

# Προσθήκη μεταβλητών χρωμάτων και εικόνας

# Εμφάνιση της εικόνας












