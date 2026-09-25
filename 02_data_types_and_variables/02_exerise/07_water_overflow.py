capacity = 255
tank = 0

n = int(input())

for _ in range(n):
    tanking = int(input())

    if tank + tanking > capacity:
        print(f"Insufficient capacity!")
        continue

    tank += tanking

print(tank)