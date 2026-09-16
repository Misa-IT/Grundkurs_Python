# Lägg till en IF-sats så att greeting inte ändras.

we_want_to_mess_with_greeting: bool = False
greeting: str = "Hej och tack! Jag blev inte borttagen!"
# Vi behöver egentligen inte skriva " == True" men jag skrev det här för att göra det
# lättare att läsa.
if we_want_to_mess_with_greeting == True:
    greeting: str = "Ånej! Jag blev ändrad!"

print(greeting)
