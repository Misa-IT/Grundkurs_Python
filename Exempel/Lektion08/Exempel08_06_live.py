# Exempel på hur man kan definiera hur man interagerar med Objekt

# Detta är ett simplistiskt exempel men i fortsättningskursen (kanske)
# man går igenom mer i detalj hur man kan använda sig av detta.

class MyObject:

    # Vi definierar vad som händer när man skapar ett nytt Objekt från
    # vår Klass (vår mall, vår ritning).
    def __init__(self, value):
        self.value = value

    # Vi definierar hur MyObject-Objekt reagerar när man försöker addera två
    # separata Instanser.
    def __add__(self, other):
        return MyObject(self.value + other.value)


# Skapa två nya objekt från mallen MyObject
object1 = MyObject(42)
object2 = MyObject(84)


print(object1 + object2)


# Vi adderar de två Objekten och skapar ett nytt Objekt med det nya värdet.
# Eftersom vi inte har förklarat för Python vad som händer när man skickar
# hela Objekt till print() så måste vi skriva ut det specifika Attributet vi
# vill ha, i detta fall det int-Objekt som ligger i våra MyObject-Objekt.
combination_object = object1 + object2
print(combination_object)
print(combination_object.value)
