# Exempel på if-satser som innehåller elif-klausuler.

siffra = 1
resultat = "ogiltigt"

if siffra >= 1:
    resultat = 1
    print("Siffra är 1")
elif siffra >= 2:
    resultat = 2
    print("Siffra är 2")
elif siffra >= 3:
    resultat = 3
    print("Siffra är 3")
elif siffra >= 4:
    resultat = 4
elif siffra >= 5:
    resultat = 5
else:
    print("Hittade inget korrekt val!")

print("resultat är", resultat)
