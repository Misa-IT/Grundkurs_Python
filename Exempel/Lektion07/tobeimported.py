# Här definierar vi saker som vi kan hämta från andra moduler.
# Lägg till _live i slutet under lektion.

def my_function():
    print("Detta skrivs ut av funktionen i tobeimported.py")


# För att förtydliga hur importfinessen fungerar visar vi ett meddelande
# här, vilket man i vanliga fall inte skulle göra i en modul som är
# tänkt att importeras.
print("Den här strängen skrivs ut i tobeimported")
print("__name__ ifrån tobeimported:", __name__)
print()

x = input("Vi sätter ett värde på x i tobeimported! Skriv in något som ska lagras här: ")
print("Vi skriver ut x medans vi är i tobeimported:", x)
print()
if __name__ == "__main__":
    print("tobeimported är main")
