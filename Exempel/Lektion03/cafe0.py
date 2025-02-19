# Original av Henrik Tunedal
# Ett exempel av ett program för ett cafe, utan samlingar.

kaffepris = 20
tepris = 15
ölpris = 50

kaffe_slutsålt = False
te_slutsålt = False
öl_slutsålt = True



beställning = input("Vad vill du beställa? ")

if beställning == "kaffe":
    produktpris = kaffepris
elif beställning == "te":
    produktpris = tepris
elif beställning == "öl":
    produktpris = ölpris
else:
    produktpris = "ERROR"


if beställning == "kaffe":
    print("Tyvärr har vi sålt slut på " + beställning + ".")
elif beställning == "te":
    print("Tyvärr har vi sålt slut på " + beställning + ".")
elif beställning == "öl":
    print("Tyvärr har vi sålt slut på " + beställning + ".")

else:
    print("Varsågod, här är ditt " + beställning + ".")
    print("Det blir", produktpris, "kr, tack.")
