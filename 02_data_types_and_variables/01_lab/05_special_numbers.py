number = input()

special_condition = [5 , 7 , 11]

def is_special(num: int) -> bool:
    return sum(int(el) for el in str(num)) in special_condition

for i in range(1, int(number) + 1):
    print(f"{i} -> {is_special(i)}")