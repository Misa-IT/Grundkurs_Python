# Exempel på vad det egentligen betyder att returnera värden.

print("Skriver ut vad som egentligen returneras av print():", print("Inre print"))
print()
x = print("Lagrar print:s returvärde i x.")
print("Värdet på x är:", x)

print()

def f(x):
    return x * 2

# Vi lagrar resultatet av f(1) i f_av_ett
f_av_ett = f(1)
# Vi tar resultatet från förra raden, skickar det till f och lagrar
# resultatet på nytt i en ny variabel.
f_av_f_av_ett = f(f_av_ett)

print("Värdet på f_av_f_av_ett är:", f_av_f_av_ett)

print("Värdet vi får tillbaka av f av f av f av f av ett,",
      "alltså 'f(f(f(f(1))))':", f(f(f(f(1))))
      )

# Det går alltså att "kedja" anrop till funktioner. Det man får tillbaka från
# den funktion som är "längst in" skickas till föregående, vilket i sin tur
# skickas till föregående och så vidare.
