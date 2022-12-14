# Vi kan skriva lite funktioner tillsammans:


# def för att meddela att vi DEFINERAR vad en ny funktion betyder.
# Namnet på funktionen bör vara lätt att förstå.
# Parenteser, (), för att de MÅSTE vara där.
# Kolon, :, för att påbörja själva definitionen.
def exempelfunktion():
    print("Vår funktion gör inget för stunden så jag lägger in lite text så länge")


# När vi vill köra vår funktion så måste vi använda parenteser efter namnet, (), för att
# meddela att vi faktiskt vill köra funktionen.
exempelfunktion()


# Om vi vill skriva en funktion som ska kunna ta emot instruktioner om vad den ska arbeta med
# så måste vi skriva det innaför parenteserna när vi DEFINERAR vår funktion.
# T.ex. Vilken text som ska skrivas ut av print() eller vilka tal som ska läggas ihop
# med en funktion som kanske heter add().
def funktion_som_tar_emot_tre_argument(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3):
    print(godtyckligt_namn1, godtyckligt_namn2, godtyckligt_namn3)

funktion_som_tar_emot_tre_argument(8,"HEJ",4.654)
