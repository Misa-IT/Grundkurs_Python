# Exempel som demonstrerar break och continue.

# Vi skapar en itereringsvariabel och en slutpunkt
i = 0
end = 10

while True:
    i += 1  # i ökas med 1 för varje varv i loopen

    # Om i når 10 så avbryter vi loopen DIREKT, inga av loopens
    # efterföljande rader körs.
    if i == end:
        break
        print("Denna rad är omöjlig att nå!")

    # Om i är 5 så avbryter vi nuvarande varvet. Loopen fortsätter men
    # kvarvarande rader i loopens kodblock hoppas över för detta varv.
    if i == 5:
        print("Hoppar över något.")
        continue
        print("Denna rad är omöjlig att nå!")

    print(i)

print("Nu är loopen över!")
