# Ett simpelt exempel av arv. Med lite om polymorfism.


class Animal:
    sound = "Jag låter som alla andra djur."

    def speak(self):
        print(self.sound)


class Dog(Animal):
    sound = "Woof!"


class Cat(Animal):
    pass


a = Animal()
fido = Dog()
pelle = Cat()

a.speak()
fido.speak()
pelle.speak()



def main():
    animals = [Dog(), Cat()]
    print(animals)
    for a in animals:
        a.speak()
    


if __name__ == "__main__":
    main()
