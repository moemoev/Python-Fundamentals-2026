number_map = {
    86: "How are you?",
    88: "Hello"
}

def return_message(n : int) -> str:
    if n in number_map:
        return f"{number_map[n]}"
    elif n < 88:
        return f"GREAT!"
    else:
        return f"Bye."

count = int(input())

for _ in range(count):
    number = int(input())
    print(return_message(number))