divisor = int(input())

boundary = int(input())

def count_down(n: int):
    i = n
    while i > 0:
        yield i
        i -= 1

for num in count_down(boundary):
    if num % divisor == 0:
        print(num)
        break
