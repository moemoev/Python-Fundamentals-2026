n = int(input())

unpure_symb = [',', '.', '_']

while n > 0:
    string = input()
    if any(string.count(el) for el in unpure_symb):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
    n -= 1