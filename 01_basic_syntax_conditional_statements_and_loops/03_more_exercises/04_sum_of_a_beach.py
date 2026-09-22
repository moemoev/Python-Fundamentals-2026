message = input().lower()

appearing_words = [
    'sand',
    'water',
    'fish',
    'sun'
]

count_words = sum([message.count(el) for el in appearing_words])

print(count_words)

