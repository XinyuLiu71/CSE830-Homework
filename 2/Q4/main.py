import heapq
from tracemalloc import take_snapshot

n = int(input())
tasks = []
heap = []
time_spent = 0

for _ in range(n):
    line = input().strip().split()
    t, l = int(line[0]), int(line[1])

    tasks.append((t, l))

tasks.sort()
# print(instructions)
# print(times)

index = 0
current_time = 0
while index < n or heap:
    if len(heap) == 0:
        current_time = max(current_time, tasks[index][0])
    
    while index < n and tasks[index][0] <= current_time:
        arrival_time, duration = tasks[index]
        heapq.heappush(heap, (duration, arrival_time))
        index += 1
    
    if heap:
        todo_long, todo_arrival = heapq.heappop(heap)
        current_time += todo_long
        time_spent += current_time - todo_arrival

print(int(time_spent/n))