# Exempel på hur man kan importera funktioner från andra
# moduler och hur man refererar till dem i koden.

import tobeimported_live

# Variabeln __name__ får olika värden beroende på vilken
# fil man startade programmet ifrån. Den modulen blir då
# "the main module", huvudmodulen.

print("Från Exempel07-01:", __name__)
print("tobeimported_live ifrån Exempel07-01-live:",
      tobeimported_live.__name__)

print()
if __name__ == '__main__':
    print("Exempel07-01-live är main")
