# Nu vill vi hämta in variabler från filen extra_exercises.py
# och definiera en ny klass som vi kan skapa objekt ifrån och lägga i de skapade
# objekten i en lista.


# Övning: Lägg till något så att vi importerar "extra_exercises" men kallar
# modulen för "exercise" i denna namnrymd.
import extra_exercises

print("Personerna från listan är:", exercise.alphabetic_list_of_first_names)


# Övning: Komplettera klassen nedan så att en persons information lagras i ett
# nytt objekt när det skapas.
class Person:
    name = str()
    age = int()
    height = int()

    def __init__(self, pers_tuple):
        self.name


# Övning: Komplettera koden nedan så att det skapas ett objekt för varje person
# från "personer" samt att varje nytt objekt läggs in i obj_personer:
obj_personer = []
for person in exercise.personer:
    pass


print("Här är alla personerna i listan:")
for person in obj_personer:
    print(person.name, person.age, person.height)




def test_person_class():
    """Funktion som kontrollerar att Person skapar korrekta objekt"""
    incorrect_init_msg = "Objekten från Person skapas inte med de korrekta attributen"

    test_person = Person(("Anna Andersson", 23, 172))
    assert test_person.name == "Anna Andersson" \
           and test_person.age == 23 \
           and test_person.height == 172, \
        incorrect_init_msg


def test_obj_personer():
    """Funktion som kontrollerar att alla personer i listan personer hamnar
    i obj_personer"""
    testpersoner = [Person(("Anna Andersson", 23, 172)),
                    Person(("Bertil Bengtsson", 27, 186)),
                    Person(("Caesar Carlander", 43, 178)),
                    Person(("David Dahlgren", 34, 177)),
                    Person(("Felicia Fagerholm", 28, 190)),
                    Person(("Emma Eriksson", 21, 185)),
                    Person(("Harold Hasselblad", 52, 184)),
                    Person(("Gustav Grip", 47, 176)),
                    ]

    assert all(
        [any([test_person.name == x.name
              and test_person.age == x.age
              and test_person.height == x.height
              for x in obj_personer])
         for test_person in testpersoner]
        ), "Alla personer från listan personer finns inte i obj_personer"


test_person_class()
test_obj_personer()
