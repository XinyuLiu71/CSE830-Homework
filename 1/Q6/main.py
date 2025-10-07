num_tests = int(input())

for test_idx in range(num_tests):
    x, y = map(int, input().split())

    d = (y // 12) - ((x - 1) // 12)
    
    s = int(y**0.5) - int((x - 1)**0.5)


    b = (int(y ** 0.5) // 6) - (int((x - 1) ** 0.5) // 6)
    
    print(f"{int(d)} {int(s)} {int(b)}")