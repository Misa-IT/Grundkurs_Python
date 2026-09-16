# Funktioner används för att separera och namnge en del av programmet, som
#   ett eget litet miniprogram, så att man kan återanvända koden.
#
# I det här exemplet skriver vi en simpel funktion som skriver ut en
#   hälsning på skärmen.
# Eftersom funktionen bara utför en utskrift och inte returnerar något
#   värde, annoterar vi returtypen som -> None.

def hello_world() -> None:
    print("Hello, World!")


# Man kan också ge Funktioner data som de behöver, i form av
#   s.k. Argument, som då inte behöver delas i hela programmet.
#
# I det här exemplet accepterar vår Funktion ett Argument, ett namn,
#   som vi sen vill att Funktionen hälsar på. Även denna har returtypen -> None.

def hello(name) -> None:
    print("Hej ", name, "!", sep="")


# För att våra Funktioner ska göra något så måste vi säga åt Python att faktiskt
#   köra dem, ovan har vi bara berättat för Python vad namnen betyder.
hello_world()
hello("Johan")


# Funktioner kan också ge värden tillbaka, vilket man kallar för att
#   RETURNERA ett värde. De liknar på det sättet Funktioner
#   inom matematiken. Det returnerade värdet hamnar därefter på samma plats i
#   koden som funktionsanropet skedde.
#
# I det här exemplet returnerar vi Argumentet multiplicerat med två.
# Eftersom funktionen returnerar ett heltal annoterar vi returtypen som -> int.
# Notera att det returnerade värdet nedan inte skrivs ut om vi inte skickar
#   det vidare till print().

def f(x) -> int:
    return x * 2
# Exemplet ovan är t.ex. väldigt likt den matematiska Funktionen f(x)=x*2


# Notera skillnaden på vad som händer på nedanstående rader.
f(1)
print(f(2))
dubblat = f(3)
print(dubblat)
f(4)
8
