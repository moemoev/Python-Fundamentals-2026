from math import trunc

data = {
    'centuries': int(input())
}
data['years'] = data['centuries'] * 100
data['days'] = trunc(data['years'] * 365.2422)
data['hours'] = data['days'] * 24
data['minutes'] = data['hours'] * 60

print(' = '.join(f"{v} {k}" for k, v in data.items()))