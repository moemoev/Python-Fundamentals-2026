sheep_queue = input().split(', ')
queue_len = len(sheep_queue)

ind_wolf = sheep_queue.index('wolf')

if ind_wolf == queue_len - 1:
    print(f"Please go away and stop eating my sheep")
else:
    sheep_in_danger = queue_len - 1 - ind_wolf
    print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!" )