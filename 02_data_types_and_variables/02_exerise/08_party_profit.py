group_size = int(input())
days = int(input())

day = 1
coins = 0

while day <= days:
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins += 50
    coins -= group_size * 2

    if day % 3 == 0:
        coins -= group_size * 3

    if day % 5 == 0:
        coins += group_size * 20

    if day % 15 == 0:
        coins -= group_size * 2



    day += 1

print(f"{group_size} companions received {coins // group_size} coins each.")