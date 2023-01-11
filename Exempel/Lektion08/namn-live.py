# Exempel som demonsterar att olika namn kan användas i olika
# sammanhang (i det här exemplet olika funktioner) för att referera till
# ett och samma objekt( i det här fallet en lista).

def lägg_till_ingredienser(bunke):
    bunke.append("ägg")
    bunke.append("mjölk")

def lägg_till_verktyg(verktygslåda):
    verktygslåda.append("hammare")
    verktygslåda.append("såg")


låda = []
lägg_till_ingredienser(låda)
lägg_till_verktyg(låda)
print(låda)


for sak in låda:
    print(sak)
