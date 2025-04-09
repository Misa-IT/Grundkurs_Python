# Exempel på hur man kan importera funktioner från andra moduler
# och hur man refererar till dem i koden.

import tobeimported

# Variabeln __name__ får olika värden beroende på vilken
# fil man startade programmet ifrån. Den modulen blir då
# "the main module", huvudmodulen.
tobeimported.my_function()
print("__name__ i Exempel07_01:", __name__)
print("__name__ i tobeimported från Exempel07_01:",
      tobeimported.__name__)

print()
if __name__ == "__main__":
    print("Exempel07_01 är main")
