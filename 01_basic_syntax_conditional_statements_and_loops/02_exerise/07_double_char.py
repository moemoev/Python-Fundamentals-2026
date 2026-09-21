token = input()

while not token == 'End':
    if not token == 'SoftUni':
        print(''.join(2 * el for el in token))

    token = input()