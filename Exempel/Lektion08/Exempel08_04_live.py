# Ett simpelt exempel av arv.

class Animal:
    sound = "Jag låter som alla andra djur."

    def speak(self):
        print(self.sound)

class Dog(Animal):
    sound = "Woof"

    def speak(self, volume):
        if volume = "Loud":
            print(self.sound + "!")
        else:
            print(sound)

class Cat(Animal):
    pass

### Vi skapar instanser av våra klasser.
##a = Animal()
##fido = Dog()
##pelle = Cat()
##
### Vi ber våra instanser att använda sin metod.
##a.speak()
##fido.speak()
##pelle.speak()

def main():
    # Vi ber våra instanser att använda sin metod.
    animals = [Dog(), Cat()]
    print(animals)
    for a in animals:
        a.speak()

if __name__ == "__main__":
    main()
