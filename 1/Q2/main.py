num_tests = int(input())

for test_idx in range(num_tests):
    line = input().split()
    S = int(line[0]) # Starting bet
    k = int(line[1]) # Number of rounds

    # Your code goes here!
    for i in range(k):
        if S % 2 == 1:
            S = S - 15
            S = S * 2
        else:
            S = S - 99
            S = S * 3
        if S < 0:
            S += 1000000
        if S > 1000000:
            S = S % 1000000

    print(S)