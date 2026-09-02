# Exempel på typannoteringar för variabler

# En typannotering visar vilken datatyp vi förväntar oss att
#   variabeln ska ha.
# Själva värdet skrivs fortfarande på samma sätt som vanligt.
user_name: str = "Alex"
age: int = 25
temperature: float = 21.5
is_ready: bool = True

print(user_name)
print(age)
print(temperature)
print(is_ready)

# Typannoteringarna har ingen faktisk effekt när programmet körs.
# De konverterar inte värden och stoppar inte programmet från att
#   använda en annan Datatyp. De är extra information för
#   människor och vissa verktyg.

# Det finns andra typer av annoteringar som vi går igenom i senare
#   lektioner.
