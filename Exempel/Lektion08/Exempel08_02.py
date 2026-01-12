# Exempel på instansvariabler och klassvariabler.

class MyClass:

    # I klassen kan vi lagra variabler.
    my_int = 42
    my_str = "HEJ"
    my_list = [1, 2]

my_instance = MyClass()

# Vi kontrollerar vad som ligger i listorna:
print("Listan i Klassen:", MyClass.my_list)
print("Listan i Instansen:", my_instance.my_list)
print()

# Vi testar att lägga till något i listan som ligger i Instansen/Objektet:
my_instance.my_list.append(3)

# Vi kollar vad som ligger i listorna
print("Listan i Klassen:", MyClass.my_list)
print("Listan i Instansen:", my_instance.my_list)
# Trots att vi bara ändrade i Instansen är det även ändrat i Klassen.
# Det är för att en variabel som ligger i en Klass delas mellan Instanser
# av den Klassen om inget annat skriver över namnet.
# Detta kallas för att vara en "klassvariabel".


# Vi skapar en Instans till för att bekräfta:
my_second_instance = MyClass()
print("Listan i den andra Instansen:", my_second_instance.my_list)
print()


# Notera skillnaden om vi gör en tilldelning istället för att använda .append():
my_instance.my_list = [4, 5]
print("Listan i Klassen:", MyClass.my_list)
print("Listan i Instansen:", my_instance.my_list)
print("Listan i den andra Instansen:", my_second_instance.my_list)
# När vi skapade listan i Instansen så blev det namnet (alltså my_list) en
# instansvariabel.
