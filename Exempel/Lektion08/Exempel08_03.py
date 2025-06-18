# Exempel på hur man kan definiera hur varje objekt som skapas från en klass
# ska se ut. Även exempel på instansvariabler och hur man definierar metoder.

class MyClass:

    my_int = 42
    my_str = "HEJ!"
    my_list = [1, 2]

    # När vi ska skapa en ny Instans/ett nytt Objekt av en Klass så anropas
    # automatiskt metoden __init__().
    # __init__() är en så kallad Konstruktor.
    # Notera att eftersom __init__() är en Metod så måste första argumentet vara
    # self.
    def __init__(self, x, y, z):
        self.my_instance_list = ["Jag ligger i en Instans."]
        self.a = x
        self.y = y
        self.z = z


my_instance = MyClass(1, 2, 3)
my_second_instance = MyClass(4, 5, 6)
print("Listan i Klassen:", MyClass.my_list)
print("Listan i första Instansen:", my_instance.my_list)
print("Listan i andra Instansen:", my_second_instance.my_list)
print()

# Nästa rad kommer att krascha programmet så efter att vi bekräftat det så
# kommenterar vi bort den.
#print("Det finns ingen inre lista i Klassen:", MyClass.my_instance_list)
print("Inre listan i första Instansen:", my_instance.my_instance_list)
print("Inre listan i andra Instansen:", my_second_instance.my_instance_list)
print()

# Vi lägger till något med .append()
my_instance.my_instance_list.append("Jag ska hamna i den första Instansens lista!")
print("Inre listan i första Instansen:", my_instance.my_instance_list)
print("Inre listan i andra Instansen:", my_second_instance.my_instance_list)
