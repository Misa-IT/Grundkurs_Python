# Här definierar vi saker som vi kan hämta från andra moduler.

def my_function():
    print("Detta skrivs ut av funktionen i tobeimported_live.py")


# För att demonstrera hur importfinessen fungerar visar vi ett meddelande
# här, vilket man i vanliga fall inte skulle göra i en modul som är
# tänkt att importeras.
print("Den här strängen skrivs ut i tobeimported_live")
print("__name__ ifrån tobeimported_live:", __name__)
print()

x = input("Vi sätter ett värde på x i tobeimported_live! Skriv in något som ska lagras här: ")
print("Vi skriver ut x medans vi är i tobeimported_live:", x)
print()

def main():
    print("tobeimported_live är main")
    
if __name__ == "__main__":
    main()
