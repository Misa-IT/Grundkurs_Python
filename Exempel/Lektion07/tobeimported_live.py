# Här definierar vi saker som vi kan hämta från andra moduler.

def my_function():
    print("Jag kommer från funktionen i tobeimported_live.py")


# För att förtydliga hur importfinessen fungerar visar vi ett meddelande
# här, vilket man i vanliga fall inte skulle göra i en modul som är
# tänkt att importeras.
print("Den här strängen ligger i tobeimported_live")

print("Från tobeimported_live:", __name__)
print()

x = input("Skriv något till Exempel07_02: ")
          
print()
if __name__ == "__main__":
    print("tobeimported_live är main:", __name__)
