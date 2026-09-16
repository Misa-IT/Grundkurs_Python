# Övning 07_08: Typannoteringar för returvärden
#
# I den här övningen ska du skriva fyra funktioner och förse varje funktion
# med en passande returtypannotering (-> Datatyp: eller -> None:).
#
# Kom ihåg:
# - Funktioner som returnerar ett värde annoteras med den datatyp de returnerar
#   (t.ex. -> int, -> str, -> bool, -> float).
# - Funktioner som inte returnerar något värde utan bara utför en handling
#   (t.ex. skriver ut med print) annoteras med -> None.


# Uppgift 1:
# Skriv en funktion med namnet `dubbla` som tar ett tal som argument,
# och returnerar talet multiplicerat med 2.
# Förse funktionen med typannoteringen -> int.

def dubbla(tal) -> int:
    # Ersätt pass med din kod här
    pass


# Uppgift 2:
# Skriv en funktion med namnet `skapa_meddelande` som tar ett namn som argument,
# och returnerar en hälsningsfras, t.ex. "Välkommen, " + namn + "!".
# Förse funktionen med typannoteringen -> str.

def skapa_meddelande(namn) -> str:
    # Ersätt pass med din kod här
    pass


# Uppgift 3:
# Skriv en funktion med namnet `ar_positiv` som tar ett tal som argument,
# och returnerar True om talet är större än 0, annars False.
# Förse funktionen med typannoteringen -> bool.

def ar_positiv(tal) -> bool:
    # Ersätt pass med din kod här
    pass


# Uppgift 4:
# Skriv en funktion med namnet `skriv_ut_linje` som inte tar några argument,
# och som skriver ut en skiljelinje med print("--------------------").
# Eftersom funktionen inte returnerar något värde, förse den med typannoteringen -> None.

def skriv_ut_linje() -> None:
    # Ersätt pass med din kod här
    pass


# Testkör dina funktioner nedan:
skriv_ut_linje()

resultat_dubbla: int = dubbla(5)
print("Dubblat värde:", resultat_dubbla)

meddelande: str = skapa_meddelande("Alex")
print(meddelande)

positivt: bool = ar_positiv(10)
print("Är 10 positivt?", positivt)

skriv_ut_linje()
