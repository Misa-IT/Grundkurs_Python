# Övning 07_03: Typannoteringar för returvärden
#
# I den här övningen ska du skriva funktioner och förse varje funktion
#    med en passande returtypannotering (-> Datatyp: eller -> None:).
#
# Kom ihåg:
# - Funktioner som returnerar ett värde annoteras med den datatyp de returnerar
#   (t.ex. -> int, -> str, -> bool, -> float).
# - Funktioner som inte returnerar något värde utan bara utför en handling
#   (t.ex. skriver ut med print) annoteras med -> None.
# - Typannoteringar för returvärden skrivs efter parametrarnas parentes
#   och före kolonet, t.ex: def min_funktion(x: int) -> int:


# ==============================================================================
# Uppgift 1: Returnera ett heltal (int)
# ==============================================================================
# Skriv klart funktionen `double` som tar emot ett heltal `number: int`.
# Funktionen ska returnera talet multiplicerat med 2.
# Lägg till returtypannoteringen `-> int` på def-raden.

def double(number: int):
    # Ersätt pass med din kod här och lägg till returtypannotering ovan
    pass


# ==============================================================================
# Uppgift 2: Returnera en textsträng (str)
# ==============================================================================
# Skriv klart funktionen `create_message` som tar emot ett namn `name: str`.
# Funktionen ska returnera en hälsningsfras, t.ex. "Välkommen, " + name + "!".
# Lägg till returtypannoteringen `-> str` på def-raden.

def create_message(name: str):
    # Ersätt pass med din kod här och lägg till returtypannotering ovan
    pass


# ==============================================================================
# Uppgift 3: Returnera ett sanningsvärde (bool)
# ==============================================================================
# Skriv klart funktionen `is_positive` som tar emot ett heltal `number: int`.
# Funktionen ska returnera True om talet är större än 0, annars False.
# Lägg till returtypannoteringen `-> bool` på def-raden.

def is_positive(number: int):
    # Ersätt pass med din kod här och lägg till returtypannotering ovan
    pass


# ==============================================================================
# Uppgift 4: Utföra en handling utan returvärde (None)
# ==============================================================================
# Skriv klart funktionen `print_line` som inte tar några argument.
# Funktionen ska skriva ut en skiljelinje: print("--------------------")
# Eftersom funktionen inte returnerar något värde ska du lägga till
#   returtypannoteringen `-> None` på def-raden.

def print_line():
    # Ersätt pass med din kod här och lägg till returtypannotering ovan
    pass


# ==============================================================================
# Testkör dina funktioner
# ==============================================================================
# Koden nedan anropar dina funktioner och skriver ut resultaten.
# Du behöver inte ändra koden nedanför denna rad.
#
# Förväntad utskrift när allt fungerar:
# --------------------
# Dubblat värde: 10
# Välkommen, Alex!
# Är 10 positivt? True
# Är -3 positivt? False
# --------------------

print_line()

doubled_value: int = double(5)
print("Dubblat värde:", doubled_value)

greeting_message: str = create_message("Alex")
print(greeting_message)

is_ten_positive: bool = is_positive(10)
print("Är 10 positivt?", is_ten_positive)

is_negative_positive: bool = is_positive(-3)
print("Är -3 positivt?", is_negative_positive)

print_line()
