
# def grade_to_letter(grade):
#     return 'lol'

# def grade_to_letter(grade):
#     "This function converts a number grade to letter"
#     if grade > 90:
#         return 'A'
#     elif grade > 80:
#         return 'B'
#     elif grade > 70:
#         return 'C'
#     else:
#         return 'F'

# print(grade_to_letter(85))
# print(grade_to_letter(77))
# print(grade_to_letter(45))
# print(grade_to_letter(100))
# print(grade_to_letter())


# def print_age(name, age):
#     "Print name with age"
#     print(name, "has", age, "years")


# print_age("Willy", 35)
# print_age("Noe", 88)
# print_age("Lucas", 78)

# def print_name_age(fulano, age=66):
#     print(fulano, "has", age, "years")


# print_name_age("Nicolas", 19)
# print_name_age("Numero 15", 19)
# print_name_age("Samuel")
# print_name_age(age=21, fulano="Roberto")
# print_name_age(fulano="Irina")

# def print_pokemon(*pokemons, *klk):
#     for pokemon in pokemons:
#         print(pokemon)


# print_pokemon("Pikachu")
# print_pokemon("Pikachu", "Charmander")
# print_pokemon("Pikachu", "Charmander", "Pidgey")
# print_pokemon("Pikachu", "Charmander", "Pidgey", "Snorlax")
# print_pokemon("Pikachu", "Charmander", "Pidgey", "Snorlax")


# def sum(lista):
#     suma = 0
#     for numero in lista:
#         suma += numero
#     return suma


# print(sum([29, 50]))

# def reversed_string(string):
# 	reversed_ = ""
# 	for i in range(len(string)-1,-1,-1):
# 		reversed_ += string[i]
# 	return reversed_

# print(reversed_string("Hola"))

# def reversed_str_while(str):
# 	reversed_ = ''
# 	len_ = len(str) - 1
# 	while len_ >= 0:
# 		reversed_ += str[len_]
# 		len_ -= 1
# 	return reversed_
# print(reversed_str_while("Hola"))


def check_range(number, lower_bound, upper_bound):
    if number >= lower_bound and number <= upper_bound:
        return True
    else:
        return False


print(check_range(7, 0, 10))
