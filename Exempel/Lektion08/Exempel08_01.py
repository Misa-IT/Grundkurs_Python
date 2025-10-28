# Exempel på hur man definierar en klass och hur man kan lagra data
# däri, vi hoppar över metoder i detta exempel.


# Vi skapar en Klass genom att använda oss av detta mönster:
# Det reserverade ordet "class".
# Namnet på vår Klass. Namnet bör börja med stor bokstav och ha en stor bokstav
# i början av varje ord. Bör inte innehålla åäö eller andra tecken som inte
# finns på ett engelskt tangentbord.
# OM vi ska ha ett arv så har man parenteser också, vi går igenom detta senare.
# Ett kolon (:) för att visa att nu börjar ett kodblock.
# En indentering på varje rad som tillhör Klassen.


class MyClass:

    # I Klassen kan vi lagra variabler.
    my_int = 42
    my_str = "HEJ"
    my_list = [1, 2]


# Om vi vill skapa en Instans av Klassen skriver vi så här:
my_instance = MyClass()

# Om vi vill komma åt t.ex. listan som ligger i Klassen så gör vi så här:
print("Listan i Klassen:", MyClass.my_list)

# Notera att vi kommer åt listan från vår nyskapade Instans/vårt Objekt:
print("Listan i Instansen:", my_instance.my_list)
