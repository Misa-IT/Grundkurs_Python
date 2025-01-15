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


class Cat(Animal):

    def __init__(self, name, prickig):
        self.name = name
        self.prickig = prickig


a = Animal()
fido = Dog("Fido")
pelle = Cat("Pelle", True)

fido.speak()
pelle.speak()

print(pelle.prickig)
print("\n\n\n")


# def main():
#     a = Animal()
#     fido = Dog("Fido")
#     pelle = Cat("Pelle", True)
#     animals = [a, fido, pelle]
#     for a in animals:
#         a.speak()
#         if a.fluffy_fur == True:
#             print("Jag har fluffig päls.")
#         else:
#             print("Jag har inte fluffig päls.")


# if __name__ == '__main__':
#     main()
