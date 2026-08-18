# Övning 07_03: Skapa och importera en egen modul
#
# I den här övningen ska du skapa en egen modul (en separat .py-fil)
# och sedan importera en funktion från den.
#
# STEG 1 — Skapa en ny fil som heter "my_greetings.py":
#   Skapa filen i SAMMA MAPP som den här filen
#   (det vill säga i mappen Övningar/Lektion07/).
#   I my_greetings.py, skriv en funktion som heter greet().
#   Funktionen ska ta emot ett argument (ett namn) och skriva ut
#   en hälsning, till exempel:
#       "Hej, Anna! Välkommen!"
#
# STEG 2 — Importera funktionen greet() här:
#   Använd "from my_greetings import greet" för att importera
#   funktionen direkt.
#
# STEG 3 — Anropa funktionen i main():
#   Be användaren skriva in sitt namn med input().
#   Skicka sedan namnet som argument till greet().
#
# Exempel på hur my_greetings.py kan se ut:
#
#   def greet(name):
#       print("Hej,", name + "! Välkommen!")
#

# --- Skriv din import här (STEG 2) ---


def main():
    # Be användaren om sitt namn och anropa greet() (STEG 3):
    name = input("Vad heter du? ")
    # Anropa greet() här:


if __name__ == "__main__":
    main()
