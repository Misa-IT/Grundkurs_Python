# Exempel på if-satser som innehåller elif-klausuler.

siffra: int = 9

resultat: str = "INTE KORREKT"

if siffra == 1:
    resultat: int = 1
    fgfdgfdgfd  # Detta ska krascha
    print("Siffra är 1")
elif siffra == 2:
    resultat: int = 2
    print("Siffra är 2")
elif siffra == 3:
    resultat: int = 3
    print("Siffra är 3")
elif siffra == 4:
    resultat: int = 4
elif siffra == 5:
    resultat: int = 5
else:
    print("Hittade inget korrekt val!")

print("Resultat är", resultat)
