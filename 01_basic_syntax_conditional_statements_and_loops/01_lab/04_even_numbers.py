count_numbers = int(input())

for _ in range(count_numbers):
    number = int(input())
    if number % 2 == 1:
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")