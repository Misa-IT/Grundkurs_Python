# Den här filen innehåller övningar på flera av delarna från grundkursen.
# Övningarna kräver att du kombinerar sådant som du har använt tidigare.
#
# Fastnar du någonstans kan du fortsätta till nästa uppgift och komma
#   tillbaka senare.
#
# OBS! Denna fil är medvetet svårare än de tidigare. Det är inte så att man
#   måste kunna lösa dessa för att gå vidare till fortsättningskursen, dessa
#   är till för att om man kan lösa dessa är man troligtvis MER än redo att
#   gå upp.
#
#   Har ni frågor om detta är det bara att höra av sig.

words = ["katt", "hund", "katt", "fågel", "hund", "hamster"]


# Övning 1: Skapa ett set som innehåller varje ord från listan words exakt
#   en gång. Skapa därefter en sorterad lista av orden i setet.
unique_words = words
sorted_unique_words = words


# Övning 2: Skriv färdigt funktionen nedan.
#
# Funktionen ska räkna ut medelvärdet av de tal som är lika med eller större
#   än en ett nytt argument som ska heta minimum. Tal under minimum ska hoppas
#   över med continue.
#
# Funktionen ska returnera en tuple med antalet använda tal och medelvärdet.
# Om inget tal kan användas ska den returnera tuplen (0, None).
# Argumentet minimum ska vara frivilligt och ha standardvärdet 0.
def summarize_numbers(numbers):
    total = 0
    count = 0

    for number in numbers:
        pass

    return count, total


# Övning 3: Skriv färdigt funktionen med en while-loop.
#
# Funktionen ska leta efter det första talet i numbers som är jämnt delbart
#   med divisor. Använd modulooperatorn (%) för att kontrollera talet och break
#   för att avsluta loopen när ett passande tal har hittats.
#
# Returnera talet som hittades, eller None om inget tal passar.
def find_first_divisible(numbers, divisor):
    index = 0
    result = None

    while index < len(numbers):
        pass

    return result


class Animal:
    number_of_legs = 4
    sound = "Jag låter som ett djur."

    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " har " + str(self.number_of_legs) + " ben."

    def speak(self):
        return self.sound


# Övning 4: Låt klassen Bird ärva från Animal.
#
# Ändra klassens attribut så att en fågel har två ben och låter "Kvitter!".
# Bird ska ärva konstruktorn och metoderna från Animal; tänk efter på om det
#   behövs skriva nya versioner av dem. När klassen är klar ska Bird("Pippi")
#   kunna skapa ett objekt med namnet "Pippi".
class Bird:
    pass


# Övning 5: Gör färdigt funktionen till ett gissningsspel.
#
# 1. Importera modulen random högst upp i filen.
# 2. Slumpa ett heltal från 1 till och med 10 med random.randint().
# 3. Ge användaren högst tre försök att gissa talet.
# 4. Använd en while-loop som frågar efter en gissning med input().
# 5. Casta svaret till int och jämför det med det slumpade talet.
# 6. Skriv om gissningen är för låg eller för hög med if/elif/else.
# 7. Avsluta loopen med break när användaren gissar rätt.
# 8. Skriv ut det rätta talet om användaren har använt alla tre försök.
def guessing_game():
    pass


def test_collections_and_functions():
    """Kontrollerar samlingarna och funktionerna ovan."""
    assert isinstance(unique_words, set), \
        "unique_words förväntades vara ett set"
    assert unique_words == {"katt", "hund", "fågel", "hamster"}, \
        "unique_words innehåller inte de efterfrågade orden"
    assert sorted_unique_words == ["fågel", "hamster", "hund", "katt"], \
        "sorted_unique_words är inte korrekt sorterad"

    assert summarize_numbers([2, -10, 4, 6]) == (3, 4), \
        "summarize_numbers() ger fel resultat med standardvärdet"
    assert summarize_numbers([2, 4, 6, 8], minimum=5) == (2, 7), \
        "summarize_numbers() hanterar inte minimum som nyckelordsargument"
    assert summarize_numbers([-3, -2, -1]) == (0, None), \
        "summarize_numbers() hanterar inte en tom beräkning"

    assert find_first_divisible([5, 9, 12, 16], 4) == 12, \
        "find_first_divisible() hittar inte det första passande talet"
    assert find_first_divisible([1, 3, 5], 2) is None, \
        "find_first_divisible() ska returnera None om inget tal passar"

    print("Samlingarna och funktionerna klarar testerna")


def test_bird_class():
    """Kontrollerar arv, attribut och ärvda metoder."""
    bird = Bird("Pippi")

    assert isinstance(bird, Animal), "Bird ärver inte från Animal"
    assert bird.name == "Pippi", "Objektet saknar rätt namn"
    assert bird.number_of_legs == 2, "En fågel förväntades ha två ben"
    assert bird.speak() == "Kvitter!", "Bird har inte rätt läte"
    assert bird.describe() == "Pippi har 2 ben.", \
        "Bird ärver inte en fungerande describe-metod"

    print("Klassen Bird klarar testerna")


def main():
    test_collections_and_functions()
    test_bird_class()
    guessing_game()


if __name__ == "__main__":
    main()
