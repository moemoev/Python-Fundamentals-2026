year = int(input())

while True:
    next_year = year + 1

    if len(set(str(next_year))) == len(str(next_year)):
        print(next_year)
        break
    year += 1