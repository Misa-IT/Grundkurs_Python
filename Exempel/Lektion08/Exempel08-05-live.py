# Ett lite mer avancerat exempel av arv.

class Animal:
    sound = "Jag låter som alla andra djur."
    number_of_legs = 4

    def speak(self):
        print(self.sound)


class Dog(Animal):
    sound = "Woof!"

    def __init__(self, name, legs=4):
        self.name = name
        self.number_of_legs = legs
        


class Cat(Animal):

    def __init__(self, name, prickig):
        self.name = name
        self.prickig = prickig



def main():
    fido = Dog("Fido")
    pelle = Cat("Pelle", True)
    animals = [fido, pelle]
    for a in animals:
        a.speak()

if __name__ == "__main__":
    main()
