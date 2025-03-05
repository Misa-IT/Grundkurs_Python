# Demonstration av hur föränderliga element i tuples fungerar.

# Vi förbereder en tuple som består av en lista och en sträng.
a_string = "Hej"
a_list = ["a", "b", "c"]
a_tuple = (a_list, a_string)
print(a_tuple)

# Ändrar vi värdena på variablerna som innehåller listan och strängen så ändras
# ingenting i vår tuple.
a_list = [1, 2, 3]
a_string = "bla"
print(a_tuple)

print()


# Vi förbereder en ny tuple, denna gång med en lista och en integer.
a_list = [1, 2, 3]
a_tuple = (a_list, 4)
print(a_tuple)

# Ändrar vi, till skillnad från ovan, på elementen i listan så syns det även
# på listan som ligger i vår tuple.
a_list[0] = 123
print(a_tuple)