
def nba_extrap(ppg, mpg):
    if ppg == 0 or mpg == 0:
        return 0
    else:
        return ppg * 48 / mpg


def fizzbuzz(n):
    while n > 0:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz', n)
        elif n % 5 == 0:
            print('Buzz', n)
        elif n % 3 == 0:
            print('Fizz')
        else:
            print(n)

        n -= 1


def printer_errors(string_control):
    errors = 0
    length = len(string_control)
    for letter in string_control:
        if letter != 'a' and letter != 'b'
            and letter != 'c' and letter != 'd'
            and letter != 'e' and letter != 'f'
            errors += 1

    return errors

    # bono 2
    return str(errors) + "/" + str(length)
