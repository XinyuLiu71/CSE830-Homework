n = int(input())

ids = {}
for i in range(n):
    id = int(input())
    if id in ids:
        ids[id] += 1
    else:
        ids[id] = 1

value = -1
max_frequency = 0
for id, f in ids.items():
    if f > max_frequency:
        value = id
        max_frequency = f
    elif f == max_frequency:
        max_value = min(value, id)
print(value)