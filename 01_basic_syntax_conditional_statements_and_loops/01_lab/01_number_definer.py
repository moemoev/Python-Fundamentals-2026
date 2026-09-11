definition = ''
number = float(input())

threshold_small = 1
threshold_large = 1000000

def set_small_or_large(num: float) -> str:
    result = ''

    if abs(num) < threshold_small:
        result = 'small '
    elif abs(num) > threshold_large:
        result = 'large '

    return result

if number == 0:
    definition = 'zero'
elif number < 0:
    definition = set_small_or_large(number) + 'negative'
else:
    definition = set_small_or_large(number) + 'positive'

print(definition)