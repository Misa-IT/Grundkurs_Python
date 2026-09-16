# Filnamnet __init__.py talar om att mappen exempelpaket är ett paket.
# Ett paket är en mapp som samlar moduler och andra paket som hör ihop.
# Koden i den här filen körs när paketet importeras.

# __all__ anger vilka namn som tas med vid import med tecknet *.
# Här pekar namnet animals på nästa paketnivå. Funktionerna i dogs.py
# finns längre ned i strukturen och blir därför inte tillgängliga direkt.
__all__ = ["animals"]
