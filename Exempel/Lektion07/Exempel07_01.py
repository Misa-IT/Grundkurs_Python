# Exempel på hur man kan importera funktioner och annat från andra
# moduler och hur man refererar till dem i koden.

import tobeimported

tobeimported.my_function()

# Variabeln __name__ får olika värden beroende på vilken
# fil man startade programmet ifrån. Den modulen blir då
# "the main module", huvudmodulen.
print("__name__ från Exempel07_01:", __name__)
print("__name__ från tobeimported i Exempel07_01:",
      tobeimported.__name__)

print()
if __name__ == "__main__":
    print("Exempel07_01 är main")
