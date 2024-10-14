# Exempel på vad det egentligen betyder att returnera värden.

print("Skriver ut värdet som returneras av print:", print("Inre print"))
x = print("Lagrar print:s returvärde i x")
print("Värdet på x är:", x)


def f(x):
    return x * 2

# Vi lagrar resultatet av f(1) i f_av_ett
f_av_ett = f(1)
# Vi tar resultatet från förra raden, skickar det till f och lagrar
# resultat på nytt i en ny variabel.
f_av_f_av_ett = f(f_av_ett)

print("Vad är", f_av_f_av_ett)

