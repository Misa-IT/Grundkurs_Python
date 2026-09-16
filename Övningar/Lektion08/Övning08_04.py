# Övning 07_04: Importera moduler från ett paket
#
# I mappen exempelpaket/animals/mammals/ finns en modul som heter dogs.py.
# Den innehåller två funktioner: bark() och bark_loudly().
#
# Just nu kraschar programmet eftersom importen nedan inte hittar dogs-modulen.
# Modulen ligger nämligen i ett underpaket (animals/mammals), inte direkt i exempelpaket.
#
# DEL 1 — Fixa importen:
#   Ändra import-raden så att bark() och bark_loudly() importeras korrekt
#       från exempelpaket.animals.mammals.dogs.
#   Tips: Använd "from ... import ..." med hela sökvägen till modulen.
#
# DEL 2 — Skapa en ny modul för kattläten:
#   1. Skapa en ny fil som heter cats.py i samma mapp som dogs.py
#      (det vill säga i exempelpaket/animals/mammals/).
#   2. I cats.py, skapa två funktioner:
#      - meow()      som skriver ut "Mjau!"
#      - meow_loudly() som skriver ut "MJAU!!"
#   3. Importera dina nya funktioner här i den här filen.
#   4. Anropa meow() och meow_loudly() i main-funktionen nedan.

from exempelpaket import *


def main():
    bark()
    bark_loudly()


main()
