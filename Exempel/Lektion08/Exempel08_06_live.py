# Ett simpelt exempel av arv. Med lite om polymorfism.

class Animal:
    sound = "Jag låter som alla andra djur."

    def speak(self):
        print(self.sound)


class Dog(Animal):
    sound = "Woof!"


class Cat(Animal):
    pass


# Vi skapar Instanser av våra Klasser.
#a = Animal()
#fido = Dog()
#pelle = Cat()
#
# Vi ber våra Instanser att använda sin metod.
#a.speak()
#fido.speak()
#pelle.speak()

def main():
    animals = [Dog(), Cat()]
    print(animals)
    for animal in animals:
        animal.speak()


if __name__ == "__main__":
    main()
