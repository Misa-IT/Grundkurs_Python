# Klasser och arv

class Animal:
    sound = "Jag låter som alla andra djur!"

    def speak(self):
        print(self.sound)


class Dog(Animal):
    # Här hämtar vi all kod från Animal
    sound = "Woof!"

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def __init__(self, name, prickig):
        self.name = name
        self.prickig = prickig


def main():
    fido = Dog("Fido")
    pelle = Cat("Pelle", True)
    print(pelle.prickig)
    animals = [fido, pelle]
    
    for a in animals:
        a.speak()
        print(a.name)

main()
