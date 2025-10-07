import os

m = int(input())
P = 32
bucket_files = []
try:
    for i in range(P):
        file_path = f"bucket_{i}.txt"
        file_obj = open(file_path, 'w', encoding='utf8')
        bucket_files.append(file_obj)

    for i in range(m):
        treasure = input().strip()
        h = hash(treasure)
        bucket_index = h % P
        bucket_files[bucket_index].write(treasure + '\n')

finally:
    for f in bucket_files:
        if not f.closed:
            f.close()

n = int(input())
queries_by_bucket = [[] for _ in range(P)]

for i in range(n):
    num = input().strip()
    h = hash(num)
    bucket_index = h % P
    queries_by_bucket[bucket_index].append(num)

count = 0
for i in range(P):
    file_path = f"bucket_{i}.txt"
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r') as f:
        good_chests_in_bucket = set(f.read().strip().splitlines())
    
    for chest_to_check in queries_by_bucket[i]:
        if chest_to_check in good_chests_in_bucket:
            count += 1
    file_obj.close()

print(count)