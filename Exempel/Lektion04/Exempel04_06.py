# Exempel som demonstrerar break och continue.

# Vi skapar en itereringsvariabel och en slutpunkt
i = 0
end = 10

# i ökas med 1 för varje varv i loopen
while True:
    i += 1
    # Om i når 10 så avbryter vi loopen DIREKT, inga av loopens
    # efterföljande rader körs.
    if i == 10:
        break
    # Om i är 5 så avbryter vi nuvarande varvet. Loopen fortsätter men
    # kvarvarande rader i loopens kodblock hoppas över för detta varv.
    if i == 5:
        continue
    print(i)

