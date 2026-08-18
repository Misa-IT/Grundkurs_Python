# Denna övning finns i två varianter:
#
# Övning07_02.py innehåller utförliga instruktioner och förklarar varje steg.
#
# Övning07_02_alternativ.py innehåller samma övning med mindre text.
#
# NI BEHÖVER BARA GÖRA EN AV DESSA. Välj den variant vars instruktioner
#   fungerar bäst för dig.
#
#
# Övning 07_02: Använda funktioner från en importerad modul
#
# I den här övningen tränar du på att importera en modul och använda
#   två av modulens funktioner. Du behöver inte kunna någon matematik
#   utantill. All information som du behöver finns i instruktionerna.
#
# Arbeta med ett steg i taget. Kör gärna programmet efter varje steg.
#
# STEG 1 — Importera modulen math
#   Ersätt hela raden med None med en import-rad.
#   Import-raden ska importera hela modulen math.
#
# STEG 2 — Hitta sidans längd
#   En kvadrat med arean 49 har sidor som är 7 långa,
#       eftersom 7 * 7 = 49.
#   Funktionen math.sqrt(49) ger därför resultatet 7.0.
#   Ersätt None efter "side_length =" med ett anrop till math.sqrt().
#   Skicka variabeln area till funktionen.
#
# STEG 3 — Avrunda ett pris uppåt
#   Att avrunda uppåt betyder att gå till nästa heltal.
#   Funktionen math.ceil(19.50) ger därför resultatet 20.
#   Ersätt None efter "rounded_price =" med ett anrop till math.ceil().
#   Skicka variabeln price till funktionen.
#
# STEG 4 — Kör programmet
#   Den första utskriften ska innehålla 7.0.
#   Den andra utskriften ska innehålla 20.

# Ersätt raden nedan med: import och modulens namn
None


# --- Dessa variabler är givna ---
area = 49
price = 19.50


def main():
    # Ersätt None med rätt funktionsanrop:
    side_length = None

    # Ersätt None med rätt funktionsanrop:
    rounded_price = None

    # Skriv ut resultaten (STEG 4):
    print("En kvadrat med arean", area, "har sidlängden", side_length)
    print("Priset", price, "avrundat uppåt blir", rounded_price)


if __name__ == "__main__":
    main()
