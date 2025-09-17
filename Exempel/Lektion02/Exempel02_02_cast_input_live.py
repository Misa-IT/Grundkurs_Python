# Exempel av att cast:a input

tal = int(input("Vilket tal ska vi dubbla? "))

print(tal * 2)
print(type(tal))
# type() är en så kallad Funktion och vi använder den här för att kontrollera
# vad för "typ" det som vi har innanför parentserna har.

tal = input("Vilket tal ska vi dubbla? ")

print("Talet vi ska dubbla är: " + tal + " vilket blir:", int(tal) * 2)
print(type(tal))
