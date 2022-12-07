my_fruits_list = ["Päron", "Äpplen", "Apelsiner", "Citroner", "Vindruvor"]

# Skriv ut hela listan
print(my_fruits_list)

# Skriv ut de tre första elementen
print(my_fruits_list[0:3])
print(my_fruits_list[:3])

# Skriv ut de tre elementen i mitten
print(my_fruits_list[1:4])

# Skriv ut de tre sista elementen
print(my_fruits_list[2:5])
print(my_fruits_list[2:])
print(my_fruits_list[-3:])
print(my_fruits_list[len(my_fruits_list)-3:])

my_details = ["Johan", "Marmén", "32", "Farsta"]

print(my_details)
print(my_details[:2])
print(" ".join(my_details[:2]))


# Slicing fungerar även på strängar
print("1234567890"[0:5])
