run: bool = True

while run:
    namn: str = input("Hej, vad heter du? ")
    if namn == "quit":
        run = False
    else:
        print("Hej, ", namn, "!")


while True:
    namn: str = input("NAMN?")
    if namn == "quit":
        break
    else:
        print("Hej, ", namn)
