num_tests = int(input())

for test_idx in range(num_tests):
    n, m, c = map(int, input().split())
    miles = 0
    fragments = 0
    wings = 0

    wings += n // m
    miles += wings
    wings = 0
    fragments += miles
    while fragments >= c:
        wings += fragments // c
        fragments = fragments % c
        miles += wings
        fragments += wings
        wings = 0

    print(miles)