# grade = int(input("Please provide the grade to evaluate: "))

# if grade > 90:
#     print('A')
# elif grade > 80:
#     print('B')
# elif grade > 70:
#     print('C')
# else:
#     print('F')


# pokemons = ['bulbasaur', 'charmander', 'squirtle']

# for pokemon in pokemons:
#     print('Current starter pokemon: ', pokemon)


# abecedary = "abcdefghijklmnopqrstuvwxyz"

# for letter in abecedary:
#     print(letter + ",")

# year = 2015
# while year < 2018:
#     print(year)
#     year += 1


year = 1990
while True:
    year += 1

    if year == 1998:
        print("1998 was the release year for Zelda: Ocarina of Time")
        continue
    elif year == 2000:
        print("New millenium!")
    elif year == 2018:
        print('Stopping program in current year')
        break

    print('year: ', year)

# move = input('Tell a rock/paper/scissors move ')

# if move == 'rock':
#     print('Rock kill scissors but die to paper')
# elif move == 'paper':
#     print('Paper kill rocks but die to scissors')
# elif move == 'scissors':
#     print('Scissors kill paper but die to rock')
# else:
#     print('Move', move, 'is invalid :(')


# for number in range(10, 0, -1):
#     if number == 8:
#         continue
#     elif number < 4:
#         break
#     print(number)

# for number in range(1, 101, 2):
#     if number % 3 == 0:
#         print("Loco, el numero", number, "es divisible entre 3.")
#         continue
#     print(number)

# year = 2015
# already_run = False
# while (not already_run) or year >= 2016:
#     already_run = True
#     print(year)
#     year += 1
