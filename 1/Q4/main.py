num_tests = int(input())

for test_idx in range(num_tests):
    x, y, n = map(int, input().split())

    result = []
    for i in range(n+1):
        result.append(i*x+(n-i)*y)

    print(" ".join(map(str, sorted(set(result)))))