def get_drink_by_age(age: int) -> str:
    if age <= 14:
        return 'toddy'
    elif age <= 18:
        return 'coke'
    elif age <= 21:
        return 'beer'
    else:
        return 'whisky'

print(f"drink {get_drink_by_age(int(input()))}")
