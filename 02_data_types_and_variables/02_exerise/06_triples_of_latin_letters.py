offset = int(input())

start = ord('a')
end = start + offset
for i in range(start, end):
    for j in range(start, end):
        for k in range(start, end):
            print(f"{chr(i)}{chr(j)}{chr(k)}")