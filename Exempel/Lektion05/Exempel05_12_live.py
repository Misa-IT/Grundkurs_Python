# Generera en multiplikationstabell med loopar inuti loopar.

table_size: int = int(input("Hur många kolumner ska vi ha? "))


row: int = 1
while row <= table_size:
    # Mata ut en rad med värden
    column: int = 1
    while column <= table_size:
        # Skriv ut varje kolumn
        number_to_print = row * column
        print(number_to_print, "\t", sep="", end="")
        
        column += 1
    print()  # För att mata ut en radbrytning för att avsluta raden

    row += 1
