run: bool = True

while run:
    namn: str = input("Hej, vad heter du? Skriv quit för att avsluta: ")
    if namn == "quit":
        run = False
    else:
        print("Hej, ", namn, "!")


while True:
    namn: str = input("NAMN? Skriv quit för att avsluta: ")
    if namn == "quit":
        break
    else:
        print("Hej, ", namn)


my_list: list = ["Äpple", "Banan", "Citron", "Dadel"]

for fruit in my_list:
    print("Dagens frukt är", fruit)