# Fortsatt från Exempel08_04.
# Nu skapar vi nya objekt från klasser och demonstrerar klasser
# som har frivilliga argument vid skapandet av instanser.

class Animal:
    sound = "Jag låter som alla andra djur."
    fluffy_fur = False

    def speak(self):
        print(self.sound)

class Dog(Animal):
    sound = "Woof"

    def __init__(self, name, fluffy_fur=True):
        self.name = name
        self.fluffy_fur = fluffy_fur
        
    def speak(self, volume):
        if volume == "Loud":
            print(self.sound + "!")
        else:
            print(sound)

class Cat(Animal):

    def __init__(self, name, prickig):
        self.name = name
        self.prickig = prickig


a = Animal()
fido = Dog("Fido")
pelle = Cat("Pelle", True)

fido.speak("Loud")
pelle.speak()

print(pelle.prickig)
