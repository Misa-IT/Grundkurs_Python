# Lägg till en IF-sats så att greeting inte ändras så länge
# we_want_to_mess_with_greeting är False.

we_want_to_mess_with_greeting: bool = False
greeting: str = "Hej och tack! Jag blev inte borttagen!"

greeting: str = "Ånej! Jag blev ändrad!"

print(greeting)
