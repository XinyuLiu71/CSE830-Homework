n = int(input())

for i in range(n):
    inputs = input().strip().split()
    diff = int(inputs[0]) - int(inputs[1])
    count = 0
    while diff:
        if diff & 1:
            count += 1
        diff >>= 1
    print(count)