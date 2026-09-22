number = int(input())


def return_larges_possible_num(num: str) -> int:
    numb_as_str = ''.join(sorted(num, reverse=True))

    return int(numb_as_str)


print(return_larges_possible_num(str(number)))
