# Den här filen innehåller övningar på flera av delarna från grundkursen.
# Övningarna kräver att du kombinerar sådant som du har använt tidigare.
#
# Fastnar du någonstans kan du fortsätta till nästa uppgift och komma
#   tillbaka senare.
#
# OBS! Denna fil är medvetet svårare än de tidigare. Det är inte så att man
#   måste kunna lösa dessa för att gå vidare till fortsättningskursen; dessa
#   är till för att om man kan lösa dessa är man troligtvis MER än redo att
#   gå upp.
#
#   Har ni frågor om detta är det bara att höra av sig.

words = ["katt", "hund", "katt", "fågel", "hund", "hamster"]


# Övning 1: Skapa en dict där varje ord från listan words är en nyckel och
#   antalet gånger ordet förekommer är nyckelns värde.
#
# Gå igenom words med en for-loop. Använd en if-sats för att kontrollera om
#   ordet redan finns i dicten och uppdatera värdet på rätt sätt.
# Skapa därefter en alfabetiskt sorterad lista av dictens nycklar.
# Det går också bra att bygga hela dicten med ett enda kort uttryck.
word_counts = {}

for word in words:
    pass

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


def test_exercise_1_count_and_sort_words():
    """Kontrollerar ordräkningen och den sorterade listan i övning 1."""
    expected_counts = {
        "katt": 2,
        "hund": 2,
        "fågel": 1,
        "hamster": 1,
    }
    expected_sorted_words = ["fågel", "hamster", "hund", "katt"]

    assert isinstance(word_counts, dict), (
        "Övning 1: word_counts ska vara en dict."
    )
    assert word_counts == expected_counts, (
        "Övning 1: word_counts ska innehålla varje ord och rätt antal."
    )
    assert isinstance(sorted_unique_words, list), (
        "Övning 1: sorted_unique_words ska vara en lista."
    )
    assert sorted_unique_words == expected_sorted_words, (
        "Övning 1: sorted_unique_words ska innehålla orden i alfabetisk ordning."
    )
    assert words == ["katt", "hund", "katt", "fågel", "hund", "hamster"], (
        "Övning 1: listan words ska inte ändras."
    )

    print("Övning 1 är korrekt löst.")


def test_exercise_2_summarize_numbers():
    """Kontrollerar urval, medelvärde och gränsfall i övning 2."""
    numbers = [2, -10, 4, 6]
    result = summarize_numbers(numbers)

    assert isinstance(result, tuple), (
        "Övning 2: summarize_numbers() ska returnera en tuple."
    )
    assert result == (3, 4), (
        "Övning 2: standardvärdet ska ta med tal som är minst 0."
    )
    assert summarize_numbers([2, 4, 6, 8], minimum=5) == (2, 7), (
        "Övning 2: minimum ska fungera som nyckelordsargument."
    )
    assert summarize_numbers([5, 6], minimum=5) == (2, 5.5), (
        "Övning 2: ett tal som är lika med minimum ska tas med."
    )
    assert summarize_numbers([-3, -2, -1]) == (0, None), (
        "Övning 2: returnera (0, None) när inget tal kan användas."
    )
    assert summarize_numbers([]) == (0, None), (
        "Övning 2: en tom lista ska ge (0, None)."
    )
    assert numbers == [2, -10, 4, 6], (
        "Övning 2: listan som skickas till funktionen ska inte ändras."
    )

    print("Övning 2 är korrekt löst.")


def test_exercise_3_find_first_divisible():
    """Kontrollerar sökningen och gränsfallen i övning 3."""
    numbers = [5, 9, 12, 16]

    assert find_first_divisible(numbers, 4) == 12, (
        "Övning 3: funktionen ska returnera det första passande talet."
    )
    assert find_first_divisible([8, 12, 16], 4) == 8, (
        "Övning 3: även det första talet i listan måste kontrolleras."
    )
    assert find_first_divisible([1, 3, 5], 2) is None, (
        "Övning 3: returnera None när inget tal passar."
    )
    assert find_first_divisible([], 3) is None, (
        "Övning 3: en tom lista ska ge None."
    )
    assert numbers == [5, 9, 12, 16], (
        "Övning 3: listan som skickas till funktionen ska inte ändras."
    )

    print("Övning 3 är korrekt löst.")


def test_exercise_4_bird_inheritance():
    """Kontrollerar arv, attribut och ärvda metoder i övning 4."""
    bird = Bird("Pippi")

    assert issubclass(Bird, Animal), (
        "Övning 4: klassen Bird ska ärva från Animal."
    )
    assert bird.name == "Pippi", (
        "Övning 4: Bird ska använda Animals konstruktor och spara namnet."
    )
    assert bird.number_of_legs == 2, (
        "Övning 4: en fågel ska ha två ben."
    )
    assert bird.speak() == "Kvitter!", (
        "Övning 4: en fågel ska låta 'Kvitter!'."
    )
    assert bird.describe() == "Pippi har 2 ben.", (
        "Övning 4: Bird ska kunna använda den ärvda metoden describe()."
    )
    assert Bird.__init__ is Animal.__init__, (
        "Övning 4: Bird ska ärva konstruktorn utan att skriva en ny."
    )
    assert Bird.describe is Animal.describe and Bird.speak is Animal.speak, (
        "Övning 4: Bird ska ärva metoderna utan att skriva nya versioner."
    )

    print("Övning 4 är korrekt löst.")


def main():
    test_exercise_1_count_and_sort_words()
    test_exercise_2_summarize_numbers()
    test_exercise_3_find_first_divisible()
    test_exercise_4_bird_inheritance()
    guessing_game()


if __name__ == "__main__":
    main()
