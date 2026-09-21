name = input()

def return_greeting(name: str) -> str:
    return f"Hello, my love!" if name == 'Johnny' else f"Hello, {name}!"

print(return_greeting(name))
