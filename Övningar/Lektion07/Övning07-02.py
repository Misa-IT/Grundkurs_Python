# Övning 07-02: Skapa en modul med funktioner för kattläten
# och lägg till anrop på den nya modulens funktioner i den här
# modulens main-funktion.
# Korrigera även importen av hundläten nedan så att den förberedda koden
# inte kraschar.

from exempelpaket import *


def main():
    bark()
    bark_loudly()


main()
