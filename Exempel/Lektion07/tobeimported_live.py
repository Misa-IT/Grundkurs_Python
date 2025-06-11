# Här definierar vi saker som vi kan hämta från andra moduler.

def my_function():
    print("Detta skrivs ut av funktionen i tobeimported_live.py")


# För att demonstrera hur importfinessen fungerar visar vi ett meddelande
# här, vilket man i vanliga fall inte skulle göra i en modul som är
# tänkt att importeras.
print("Den här strängen skrivs ut i tobeimported_live")
print("__name__ ifrån tobeimported:", __name__)
print()


def main():
    print("tobeimported_live är main")


if __name__ == "__main__":
    main()
