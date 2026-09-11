budget = int(input())

token = input()

while not token == 'End':
    budget -= int(token)

    if budget < 0:
        print(f"You went in overdraft!")
        break

    token = input()

else:
    print("You bought everything needed.")

