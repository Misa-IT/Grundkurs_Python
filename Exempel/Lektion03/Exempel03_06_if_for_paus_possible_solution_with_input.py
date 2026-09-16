# Lägg till en IF-sats så att greeting inte ändras.

we_want_to_mess_with_greeting: str = input("Vill vi att greeting ändras? True eller False: ")
greeting: str = "Hej och tack! Jag blev inte borttagen!"

if we_want_to_mess_with_greeting == "True":
    greeting: str = "Ånej! Jag blev ändrad!"

print(greeting)
