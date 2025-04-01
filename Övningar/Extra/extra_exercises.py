# Den här filen ska kunna importeras från ÖvningExtra-02 och ÖvningExtra-03.py.

# I den här filen så finns en rad uppgifter. Vissa bygger på varandra och
# vissa måste lösas för att ÖvningExtra-02 ska fungera. Fastnar ni nånstans,
# fortsätt till nästa uppgift och kom tillbaka senare så kanske ni kommer
# på en ny lösning.

# Glöm inte att göra uppgifterna i main(), nedan; det är fem (5) uppgifter i
# denna fil.


personer = [("Anna Andersson", 23, 172), ("Bertil Bengtsson", 27, 186),
            ("Harold Hasselblad", 52, 184), ("Gustav Grip", 47, 176),
            ("Felicia Fagerholm", 28, 190), ("Emma Eriksson", 21, 185),
            ("Caesar Carlander", 43, 178), ("David Dahlgren", 34, 177),
            ]


# Övning: Skriv om raden nedan så att list_of_names bara innehåller namnen på
# de personer som finns i listan "personer" och inte deras övriga information.
list_of_names = personer


# Övning: Skriv om koden nedan så att listan alphabetic_list_of_first_names
# endast innehåller personers förnamn och att de står i alfabetisk ordning.
# Det går att lösa på bara en rad men upp till åtta är rimligt.
# (Ni kan döpa om listan, det långa namnet är bara för tydlighet. Glöm inte
# att ändra i main() i så fall.)
alphabetic_list_of_first_names = personer


# Övning: Den här funktionen ska kunna hämta ut en specifik person från listan personer
# och returnera en lista med den personens information (namn, ålder och längd).
# Komplettera nedanstående kod så att man får ut en lista med en persons
# information istället för en lista om alla personer eller en tuple om bara en person.
def personal_info(lista, vem):
    info = lista
    vem
    return info


def main():

    print("Om du ser den här texten när du kör programmet från ÖvningExtra-02"
          " har något gått snett.")

    # Övning: Skriv färdigt den här loopen så att det skrivs ut hela meningar
    # med namn, ålder och längd om varje person.
    for p in personer:
        print("är""år gammal""cm lång.")

    # Övning: Skriv färdigt den här loopen så att vi får ut en lista över
    # namnen, och endast namnen, på de som är äldre än 30år i den print() som
    # kommer efter loopen.
    over_30 = []
    #in personer:

    print("De som är över 30 ifrån listan är: ", over_30)

    print("En alfabetisk lista av personers förnamn:", alphabetic_list_of_first_names)
    print("Här ska du se information om Bertil:", personal_info(personer, "Bertil"))

    # Nästa rad kontrollerar att personal_info() samt listorna uppfyller det
    # som övningarna ber om.
    test_personal_info()
    test_lists()






def test_personal_info():
    """En funktion som kontrollerar att funktionen personal_info() returnerar
    korrekta värden."""
    bertil_info = ["Bertil Bengtsson", 27, 186]
    personal_return = personal_info(personer, "Bertil")
    wrong_type_msg = "personal_info() returnerar  inte en lista"
    wrong_contents_msg = "Returvärdet från personal_info() innehåller inte det som efterfrågas."

    assert isinstance(personal_return, list), wrong_type_msg
    assert personal_return == bertil_info, wrong_contents_msg
    print("personal_info() klarar testerna")

def test_lists():
    """En funktion som kontrollerar att listorna är korrekta."""
    names = ['Anna Andersson', 'Bertil Bengtsson', 'Caesar Carlander', 'David Dahlgren',
             'Felicia Fagerholm', 'Emma Eriksson', 'Harold Hasselblad', 'Gustav Grip']
    alpha_first = ['Anna', 'Bertil', 'Caesar', 'David', 'Emma', 'Felicia', 'Gustav', 'Harold']
    lists = [list_of_names, alphabetic_list_of_first_names]
    list_names = ["list_of_names", "alphabetic_list_of_first_names"]
    contents = [names, alpha_first]

    for list_, contents, list_name in zip(lists, contents, list_names):
        assert isinstance(list_, list), f"{list_name} förväntades vara en lista"
        assert list_ == contents, f"Listan {list_name} innehåller det inte det som efterfrågades"

    print("Listorna klarar testerna")

if __name__ == '__main__':
    main()
