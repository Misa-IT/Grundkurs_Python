while True:
    namn = input("Hej, vad heter du? ")
    if namn == "quit":
        break
    else:
        print("Hej,", namn)

run = True

while run == True:
    namn = input("Vad heter du? ")
    if namn == "quit":
        run = False
    else:
        print("Hej,", namn)
