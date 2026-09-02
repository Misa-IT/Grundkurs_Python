# Exempel av input()

# input() visar en sträng för användaren, en så kallad prompt,
#   som bör uppmana användaren att skriva in ett svar.
# Svaret hämtas som en sträng, alltås som text, och kan sen lagras
#   lagras i en variabel eller anvädnas direkt.


print("Hej, vad heter du?")

user_name = input("Mitt namn är: ")

print("---------")

user_name = input("Hej, vad heter du?\nMitt namn är: ")

print("Trevligt att träffas, " + user_name + ".")
