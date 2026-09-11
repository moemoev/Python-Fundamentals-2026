size = int(input())

def print_upper_half(n: int) -> str:
    result = ''

    for i in range(1, n + 1):
        result += i * '*'
        result += '\n'

    return result

def print_lower_half(n:int) -> str:
    result = ''

    for i in range(n - 1 , 0, -1):
        result += i * '*'
        result += '\n'

    return result.rstrip()

print(print_upper_half(size) + print_lower_half(size))
