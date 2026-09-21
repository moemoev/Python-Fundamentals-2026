keys = [
    'coding',
    'dog',
    'cat',
    'movie'
]

token = input()

count_coffee = 0

while not token == 'END':
    if token.lower() in keys:
        count_coffee += 1 if token == token.lower() else 2

    if count_coffee > 5:
        print(f"You need extra sleep")
        break
    token = input()

else:
    print(count_coffee)