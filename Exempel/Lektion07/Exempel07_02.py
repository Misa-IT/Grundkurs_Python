# Första gången vi importerar en modul i vårt program laddas
# den från disk och koden i modulen körs.
# Lägg till _live i slutet under lektion.

print("Importerar modulen tobeimported...")
import tobeimported
print("Importerad modul:", tobeimported)

# Observera att koden i tobeimported inte körs andra gången,
# om vi importerar modulen igen eftersom vi har laddat den
# tidigare.
print()

y = input("Vi väntar på att du ska ändra något i tobeimported.")

print()
print("Importerar samma modul igen!")
import tobeimported
print("Fortfarande samma modul:", tobeimported)
