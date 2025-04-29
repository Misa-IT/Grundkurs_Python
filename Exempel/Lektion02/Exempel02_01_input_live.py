# Exempel av input()

# input()visar en sträng för användaren, en så kallad prompt,
# som bör uppmana användaren att skriva in ett svar.
# Svaret hämtas som en sträng, alltså som text, och kan sen sparas i en variabel
# eller användas direkt.

print("Hej, vad heter du?")

user_name = input("Mitt namn är: ")

user_name = input("Hej, vad heter du?\nMitt namn är: ")

print("Trevligt att träffas, " + user_name + ".")
