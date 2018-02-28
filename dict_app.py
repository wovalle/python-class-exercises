usernames = {}
def save_to_file(dict):
    with open('db.txt', 'w') as file:
        for name, uname in dict.items():
            file.write('%s,%s\n' % (name, uname))

def read_from_file():
    with open('db.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            n, u =  line.strip().split(',')
            usernames[n] = u


read_from_file()
while True:
    print('''
        Insert a command:
        search: search username
        list: list all the names in the system
        quit: Exits the program
        ''')

    command = input()

    if command == 'quit':
        print('Goodbye 👋🏼')
        exit()
    elif command == 'list': 
        for key, value in usernames.items():
            print('%s is the username of %s' % (value, key))
    elif command == 'search':
        print('Enter a name:')
        name = input()
        if name in usernames:
            print(usernames[name] + ' is the username of ' + name)
        else:
            print('I don\'t have ' + name + '\'s username, what is it?')
            username = input()
            usernames[name] = username
            save_to_file(usernames)
            print('Data updated.')
    else:
        print('Command "%s" is invalid.' % command)
