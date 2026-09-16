# Jämförelse av while och for med en lista.
# Ibland kan man använda den typ av loop man föredrar.

my_int_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i: int = 0
while i < len(my_int_list):
    element = my_int_list[i]
    i += 1
    print(element)

print()

for element in my_int_list:
    print(element)
