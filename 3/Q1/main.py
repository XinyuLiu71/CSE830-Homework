n = int(input())


diff_list = []
for i in range(n):
    inputs = input().strip().split()
    gained, lost = int(inputs[0]), int(inputs[1])

    diff_list.append(gained-lost)

for start in range(n):
    health = 0
    for step in range(n):
        health += diff_list[(start+step)%n]
        if health < 0:
            break
    if step == n-1:
        break
print(start)