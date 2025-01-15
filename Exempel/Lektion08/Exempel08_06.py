# Exempel på hur man kan definiera hur man interagerar med objekt

# Detta är ett simplistiskt exempel men i fortsättningskursen (kanske)
# man går igenom mer i detalj hur man kan använda sig av detta.

# DONT COPY: VARNING: Det här kan bli ganska avancerat mot slutet.

class MyObject:

    # Vi definierar vad som händer när man skapar ett nytt objekt från
    # vår klass (vår mall, vår ritning).
    def __init__(self, value):
        self.value = value

    # Vi definierar hur MyObject-objekt reagerar när man försöker addera två
    # separata instanser.
    def __add__(self, other):
        return MyObject(self.value + other.value)


# Skapa två nya objekt från mallen MyObject
object1 = MyObject(42)
object2 = MyObject(84)


# Vi adderar de två objekten och skapar ett nytt objekt med det nya värdet.
# Eftersom vi inte har förklarat för Python vad som händer när man skickar
# hela objektet till print() så måste vi skriva ut det specifika värdet vi vill
# ha, i detta fall det int-objekt som ligger i vårt MyObject-objekt.
combination_object = object1 + object2
print(combination_object)
print(combination_object.value)
