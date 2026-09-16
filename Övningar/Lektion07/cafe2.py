# Orignal av: Henrik Tunedal
# Ett exempel av ett program för ett cafe, med listor.

produkter = ["kaffe", "te", "öl"]
priser = [20, 15, 50]
slutsålt = [False, False, True]


def produktpris(produkt):
    index = 0
    for p in produkter:
        if p == produkt:
            return priser[index]
        else:
            index += 1


def produkt_slutsåld(produkt):
    index = 0
    for p in produkter:
        if p == produkt:
            return slutsålt[index]
        else:
            index += 1


beställning = input("Vad vill du beställa? ")

if produkt_slutsåld(beställning):
    print("Tyvärr har vi sålt slut på " + beställning + ".")
else:
    pris = produktpris(beställning)
    print("Varsågod, här är ditt " + beställning + ".")
    print("Det blir", pris, "kr, tack.")
