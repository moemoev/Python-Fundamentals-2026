n = int(input())

# snowballs = []
#
# for _ in range(n):
#     weight = int(input())
#     time = int(input())
#     quality = int(input())
#     value = (weight // time) ** quality
#     snowballs.append([ value, f"{weight} : {time} = {value} ({quality})"])
#
# snowballs.sort(key=lambda x: x[0], reverse=True)
#
# print(snowballs[0][1])

value = 0
calculation = ''

for _ in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    key = (weight // time) ** quality

    if key > value:
        value = key
        calculation = f"{weight} : {time} = {value} ({quality})"

print(f"{calculation}")