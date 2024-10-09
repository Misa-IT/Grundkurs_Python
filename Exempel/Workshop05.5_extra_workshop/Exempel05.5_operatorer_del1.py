# Exempel på tilldelningsoperatorerna samt demonstration av förstärkt tilldelning:

# Vanlig tilldelning, vi berättar för Python vad som ska lagras med ett visst
# namn:
a = 42
print("Vi har tilldelat a värdet:", a)


# Förstärkt tilldelning (Augmented assigment), vi ber Python att ändra på något
# eller att basera den nya tilldelningen på det gamla värdet:

b = 42
b += 1
print("Vi har tilldelat b sitt gamla värde plus ett:", b)

c = 42
c -= 1
print("Vi har tilldelat c sitt gamla värde minus ett:", c)

d = 42
d *= 2
print("Vi har tilldelat d sitt gamla värde gånger två:", d)

e = 42
e /= 2
print("Vi har tilldelat e sitt gamla värde gånger två:", e)

# Och så vidare. Alla "instruktionsoperatorerna" kan kombineras med ett = för
# att skapa en förstärkt tilldelning.


# En viktig aspekt med förstärkt tilldelning: Om variabeln är av en datatyp
# som är föränderlig så ändrar man på det som ligger där, istället för att
# skriva över det gamla värdet.

print("\n\n")  # För att skapa utrymme i utskriften.

# I vanlig tilldelning, eller om datatypen är oföränderlig, så skrivs det gamla
# värdet över helt och sparas på en annan plats i datorns minne.
x = 42
x_id1 = id(x)
print(x_id1, "är minnesadressen till x som har värdet:", x)

x = x + 1
x_id2 = id(x)
print(x_id2, "är minnesadressen till x efter att ha gjort en ny tilldelning. Nya värdet är:", x)
print("Vi kollar om adresserna är identiska:", x_id1 == x_id2)


print()  # För att skapa utrymme i utskriften.


x = 42
x_id1 = id(x)
print(x_id1, "är minnesadressen till x som har värdet:", x)
x += 1
x_id2 = id(x)
print(x_id2, "är minnesadressen till x efter att ha gjort en förstärkt tilldelning. Nya värdet är:", x)
print("Vi kollar om adresserna är identiska:", x_id1 == x_id2)

print("\n\n")  # För att skapa utrymme i utskriften.

# Integers är oföränderliga; även om vi gör en förstärkt tilldelning så hamnar
# det nya värdet på en annan plats i datorn.


# Om variabeln är av en datatyp som är föränderlig så ändras värdet på variabeln
# utan att flytta på adressen.
x = [1, 2]
x_id1 = id(x)
print(x_id1, "är minnesadressen till x som har värdet:", x)

x = x + [3, 4]
x_id2 = id(x)
print(x_id2, "är minnesadressen till x efter att ha gjort en ny tilldelning. Nya värdet är:", x)
print("Vi kollar om adresserna är identiska:", x_id1 == x_id2)


print()  # För att skapa utrymme i utskriften.

x = [1, 2]
x_id1 = id(x)
print(x_id1, "är minnesadressen till listan x som har värdet:", x)
x += [3, 4]
x_id2 = id(x)
print(x_id2, "är minnesadressen till x efter att ha gjort en förstärkt tilldelning. Nya värdet är:", x)
print("Vi kollar om adresserna är identiska:", x_id1 == x_id2)
