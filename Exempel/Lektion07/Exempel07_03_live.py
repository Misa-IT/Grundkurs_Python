# Första gången vi importerar en modul i vårt program laddas
# den från disk och koden i modulen körs.

print("Importerar modulen tobeimported_live...")
import tobeimported_live
print("Importerad modul:", tobeimported_live)

# Observera att koden i  tobeimported_live inte körs andra gången,
# om vi importerar modulen igen eftersom vi har laddat den
# tidigare.
print()

y = input("Vi väntar på att du ska ändra något i tobeimported_live.")

print()
print("Importerar samma modul igen!")
import tobeimported_live
print("Fortfarande samma modul:", tobeimported_live)
