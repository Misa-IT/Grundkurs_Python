siffra = int(input("Vad är siffran? "))
resultat = "Felaktigt!"

if siffra == 1:
    resultat = 1
    print("Siffra är 1")
elif siffra <= 2:
    resultat = 2
    print("Siffra är 2")
elif siffra <= 3:
    resultat = 3
    print("Siffra är 3")
else:
    print("Hittade inget korrekt val!")

print("Resultat är:", resultat)
