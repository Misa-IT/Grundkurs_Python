# Exempel på hur man kan definera hur varje objekt som skapas från en klass
# ska se ut. Även exempel på instansvarabler.

class MyClass:
    my_int = 42
    my_str = "HEJ"
    my_list = [1, 2]

# När vi ska skapa en ny instans/ett nytt objekt av en klass så anropas
# automatiskt metoden __init__.
# __init__ är en så kallad Konstruktör.
# Notera att eftersom __init__ är en metod så måste första argumentet vara self.
    def __init__(self):
        self.my_instance_list = ["Jag ligger i en instans"]

my_instance = MyClass()
my_second_instance = MyClass()
print("Listan i klassen:", MyClass.my_list)
print("Listan i första instansen:", my_instance.my_list)
print("Listan i andra instansen:", my_second_instance.my_list)
print()
#print("Det finns ingen instanslista i klassen:", MyClass.my_inner_list)
print("Instanslistan i första instansen:", my_instance.my_instance_list)
print("Instanslistan i andra instansen:", my_second_instance.my_instance_list)
print()
# Vi ändrar på instanslistan i den första instansen:
my_instance.my_instance_list.append("Jag ska hamna i den första instansens lista!")
print("Instanslistan i första instansen:", my_instance.my_instance_list)
print("Instanslistan i andra instansen:", my_second_instance.my_instance_list)
