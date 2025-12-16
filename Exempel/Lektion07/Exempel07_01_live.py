# Exempel på hur man kan importera funktioner och annat från andra
# moduler och hur man refererar till dem i koden.

import tobeimported_live

tobeimported_live.my_function()

# Variabeln __name__ får olika värden beroende på vilken
# fil man startade programmet ifrån. Den modulen blir då
# "the main module", huvudmodulen.
print("__name__ från Exempel07_01_live:", __name__)
print("__name__ från  tobeimported_live i Exempel07_01_live:",
      tobeimported_live.__name__)

print()
if __name__ == "__main__":
    print("Exempel07_01_live är main")
