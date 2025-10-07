n = int(input())
stack = []
max_stack = []
for i in range(n):
    op = input().strip()
    if len(op.split(' ')) == 1:
        op = int(op)
        if op == 2:
            stack.pop()
            max_stack.pop()
        elif op == 3:
            print(max_stack[-1])
    else:
        importance = int(op.split(' ')[1])
        stack.append(importance)
        if len(max_stack) == 0 or importance >= max_stack[-1]:
            max_stack.append(importance)
        elif importance < max_stack[-1]:
            max_stack.append(max_stack[-1])