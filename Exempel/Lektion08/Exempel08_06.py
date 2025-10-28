# Exempel på hur man kan definiera hur man interagerar med Objekt

# Detta är ett simplistiskt exempel men i fortsättningskursen (kanske)
# man går igenom mer i detalj hur man kan använda sig av detta.

# DONT COPY: VARNING: Det här kan bli ganska avancerat mot slutet.

class MyClass:

    # Vi definierar vad som händer när man skapar ett nytt Objekt från
    # vår Klass (vår mall, vår ritning).
    def __init__(self, value):
        self.value = value

    # Vi definierar hur MyClass-Objekt reagerar när man försöker addera två
    # separata Instanser.
    def __add__(self, other):
        return MyClass(self.value + other.value)


# Skapa två nya Objekt från mallen/Klassen MyClass
object1 = MyClass(42)
object2 = MyClass(84)


# Vi adderar de två Objekten och skapar ett nytt Objekt med det nya värdet.
# Eftersom vi inte har förklarat för Python vad som ska hända när man
# skickar Instanser av vår Klass till print()  så måste vi skriva ut det
# specifika Attributet vi vill ha, i detta fall det int-Objekt som ligger i
# vårt MyClass-objekt.
combination_object = object1 + object2
print(combination_object)
print(combination_object.value)
