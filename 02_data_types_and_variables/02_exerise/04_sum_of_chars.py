n = int(input())

sum_chars = sum(ord(input()) for i in range(n))

print(f"The sum equals: {sum_chars}")
