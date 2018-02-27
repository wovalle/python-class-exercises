usernames = {'pablo': 'numero_1', 'roberto': 'snow'}

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
            print('Data updated.')
    else:
        print('Command "%s" is invalid.' % command)
