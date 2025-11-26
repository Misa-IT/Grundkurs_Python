# Generera en multiplikationstabell med loopar inuti loopar.

table_size = int(input("Hur många kolumner ska vi ha? "))
# kolumnbredd = 5

rad = 1
while rad <= table_size:
    # Mata ut en rad med värden
    kolumn = 1
    while kolumn <= table_size:
        # Skriv ut varje kolumn
        #print(str(rad * kolumn).ljust(kolumnbredd), end="")
        print(str(rad * kolumn), "\t", sep="", end="")
        kolumn += 1
    print()   # För att mata ut en radbrytning för att avsluta raden

    rad += 1
