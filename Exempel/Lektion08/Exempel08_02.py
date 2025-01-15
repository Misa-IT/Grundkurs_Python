# Exempel på instansvariabler och klassvariabler.

class MyClass:

    # I klassen kan vi lagra variabler.
    my_int = 42
    my_str = "HEJ"
    my_list = [1, 2]


# Om vi vill skapa en INSTANS av klassen skriver vi så här:
my_instance = MyClass()

# Notera att det finns en lista i vår nyskapade instans/vårt objekt.
print("Listan i instansen:", my_instance.my_list)
print()

# Vi testar att lägga till något i listan som ligger i instansen/objektet.
my_instance.my_list.append(3)

# Vi kollar vad som ligger i listan i instansen och vad som ligger i klassen.
print("Listan i instansen:", my_instance.my_list)
print("Listan i klassen:", MyClass.my_list)
# Trots att vi bara ändrade i instansen är det även ändrat i klassen.
# Det är för att en variabel som ligger i en klass delas mellan alla instanser
# av den klassen om man inte skriver över namnet.
# Detta kallas för att vara en "klassvariabel".


# Vi skapar en instans till för att bekräfta:
my_second_instance = MyClass()
print("Listan i den andra instansen:", my_second_instance.my_list)
print()


# Notera skillnaden om vi gör en tilldelning istället för att använda .append():
my_instance.my_list = [4, 5]
print("Listan i instansen:", my_instance.my_list)
print("Listan i klassen:", MyClass.my_list)
print("Listan i den andra instansen:", my_second_instance.my_list)
