inputs = input().strip().split()
N, k = int(inputs[0]), int(inputs[1])

top_list = []
for i in range(N):
    animal = int(input())
    if not top_list or (len(top_list) < k and top_list[-1] >= animal):
        top_list.append(animal)
    elif len(top_list) < k or top_list[-1] <= animal:
        for j in range(len(top_list)):
            if top_list[j] <= animal:
                top_list[j+1:] = top_list[j:]
                top_list[j] = animal
                top_list = top_list[:k]
                break
# print(f"len:{len(top_list)}")
for i in top_list:
    print(i)