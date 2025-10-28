# Ett exempel på fler av specialmetoderna man kan lägga in i egenskapade
# Klasser och hur man kan lägga in kod som förhindrar vanliga fel från
# att uppstå.

# Detta är inte exakt hur man bör göra för att förhindra dessa fel, men hur
# man bör göra går man igenom i fortsättningskursen. Exception handling,
# om ni vill läsa om det på egen hand.


class MyClass:

    # Konstruktorn
    def __init__(self, value):
        self.value = value

    # Hur Objekt ska reagera på operatorn +
    def __add__(self, other):

        #if type(self) == type(other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        else:
            return "Ogiltig operation"

    # Hur Objekt ska reagera på operatorn ==
    def __eq__(self, other):
        return self.value == other.value

    # Vad Objekt ska returnera när något ber om en sträng-representation av
    # Obejektet
    def __str__(self):
        return str(self.value)

a = MyClass(2)
b = MyClass(2)
c = a
# Vi jämför Objekten
print("a == b:", a == b)
print("a == c:", a == c)
print("a is b:", a is b)
print("a is c:", a is c)
print()
