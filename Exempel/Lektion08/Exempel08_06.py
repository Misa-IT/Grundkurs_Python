# Exempel på hur man importerar moduler som ligger i mappar.
# Även hur det ser ut när man importerar paket.
# Original av: Henrik Tunedal

print("Här börjar programmet och dess modulnamn är:", __name__)

import exempelpaket
import exempelpaket.extragrejer

exempelpaket.extragrejer.mitt_namn()

print("Klart!")

exempelpaket.tjosan()
