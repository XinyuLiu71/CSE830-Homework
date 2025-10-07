num_birds = int(input())
distance_line = input().strip()
distances = [int(x) for x in distance_line.split()]

distances.sort()

i = 0
print(num_birds)
while i < num_birds:
    value = distances[i]
    j = i + 1
    while j < num_birds:
        if distances[j] == value:
            j += 1
        else:
            i = j - 1
            print(num_birds - j)
            break
    i += 1