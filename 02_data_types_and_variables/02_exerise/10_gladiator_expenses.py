n = int(input())

prices = {
    'helmet': float(input()),
    'sword': float(input()),
    'shield': float(input()),
    'armor': float(input()),
}

expenses = 0.0
count_shield_repairs = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        expenses += prices['helmet']

    if i % 3 == 0:
        expenses += prices['sword']

    if i % 6 == 0:
        expenses += prices['shield']
        count_shield_repairs += 1

        if count_shield_repairs == 2:
            expenses += prices['armor']
            count_shield_repairs = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")