# Den här koden kör oändligt.
# Rätta till den så att det inte längre händer.

# MEN programmets funktionalitet ska inte ändras!
# D.v.s:
# Loopen ska vara kvar.
# Specifikt raden "while my_int < amount:" ska INTE ändras.
# Funktionen ska fortfarande skriva ut ett värde och returnera my_inner_int + 1.

# Tips: Här har man nytta av att använda sig av typannotationer.

def print_and_increment(my_inner_int):
    print(my_inner_int)
    return my_inner_int + 1


amount: int = int(input("Hur många gånger ska jag köra? "))
my_int: int = 0
while my_int < amount:
    print_and_increment(my_int)
