# Original av: Henrik Tunedal

antal_te = 0
antal_kaffe = 0
antal_rooibos = 0

# Detta använder tilldelningsoperatorn :=, även kallad walrusoperatorn.
# Det är ett frivilligt, kortare skrivsätt och inte något ni behöver använda.
# Ett vanligt sätt att skriva samma sak är:
#
# while True:
#     dryck = input("Önskad dryck? ")
#     if not dryck:
#         break
#     # Hantera valet av dryck här.

while dryck := input("Önskad dryck? "):
    if dryck == "te":
        antal_te += 1
    elif dryck == "kaffe":
        antal_kaffe += 1
    elif dryck == "rooibos":
        antal_rooibos += 1

print(antal_te, "personer vill ha te.")
print(antal_kaffe, "personer vill ha kaffe.")
print(antal_rooibos, "personer vill ha rooibos.")
