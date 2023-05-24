# Vi skriver lite funktioner tillsammans:


# def för att meddela att vi DEFINERAR vad en ny funktion betyder.
# Namnet på funktionen bör vara lätt att förstå och BÖR inte innehålla åäö.
# Parenteser, (), för att de MÅSTE vara där även om vi inte planerar att använda
# argument med denna funktion.
# Kolon, :, för att påbörja själva definitionen.
def exempelfunktion():
    print("Vår funktion gör inget för stunden så jag lägger in lite text så länge")


# När vi vill köra vår funktion så måste vi använda parenteser, (),
# för att meddela att vi faktiskt vill köra funktionen.
exempelfunktion()


# Om vi vill skriva en funktion som ska kunna ta emot instruktioner om vad den
# ska arbeta med så måste vi skriva det innanför parenteserna när vi
# DEFINERAR vår funktion.
# T.ex. vilken text som ska skrivas ut av print() eller vilka tal som ska
# läggas ihop av en funktion som adderar två tal.
def funktion_som_tar_emot_tre_argument(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3):
    print(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3)


# Det som vi skrev innanför parenteserna i DEFINITIONEN är alltså vad vi namnger
# det som skickas till vår funktion som argument när vi kallar på den.

funktion_som_tar_emot_tre_argument(8, "HEJ", 4.567)
