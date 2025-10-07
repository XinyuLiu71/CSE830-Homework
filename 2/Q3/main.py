import sys

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.map = {}

    def _swap(self, i, j):
        val_i, val_j = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = val_j, val_i
        self.map[val_i].remove(i)
        self.map[val_i].add(j)
        self.map[val_j].remove(j)
        self.map[val_j].add(i)

    def _sift_up(self, i):
        parent_index = (i - 1) // 2
        while i > 0 and self.heap[i] > self.heap[parent_index]:
            self._swap(i, parent_index)
            i = parent_index
            parent_index = (i - 1) // 2

    def _sift_down(self, i):
        size = len(self.heap)
        while True:
            max_index = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if left_child < size and self.heap[left_child] > self.heap[max_index]:
                max_index = left_child
            if right_child < size and self.heap[right_child] > self.heap[max_index]:
                max_index = right_child
            
            if max_index == i:
                break
            
            self._swap(i, max_index)
            i = max_index

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        if value not in self.map:
            self.map[value] = set()
        self.map[value].add(i)
        self._sift_up(i)

    def pop(self):
        if not self.heap:
            return None
        top_value = self.heap[0]
        self.delete(top_value)
        return top_value

    def delete(self, value):
        if value not in self.map or not self.map[value]:
            return False

        index_to_delete = self.map[value].pop()
        if not self.map[value]:
            del self.map[value]

        size = len(self.heap)
        last_val = self.heap.pop()

        if index_to_delete == size - 1:
            return True

        self.heap[index_to_delete] = last_val
        self.map[last_val].remove(size - 1)
        self.map[last_val].add(index_to_delete)

        parent_index = (index_to_delete - 1) // 2
        if index_to_delete > 0 and self.heap[index_to_delete] > self.heap[parent_index]:
            self._sift_up(index_to_delete)
        else:
            self._sift_down(index_to_delete)
        
        return True
    
    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


max_heap = MaxHeap() # For the smaller half of numbers
min_heap = MaxHeap() # For the larger half (storing them as negatives to use MaxHeap)

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().strip().split()
    op, x = line[0], int(line[1])

    if op == 'a':
        if max_heap.size() == 0 or x <= max_heap.peek():
            max_heap.push(x)
        else:
            min_heap.push(-x)

    elif op == 'r':
        if not (max_heap.delete(x) or min_heap.delete(-x)):
            print("Wrong!")
            continue

    if max_heap.size() > min_heap.size() + 1:
        val = max_heap.pop()
        min_heap.push(-val)
    elif min_heap.size() > max_heap.size():
        val = -min_heap.pop()
        max_heap.push(val)

    total_size = max_heap.size() + min_heap.size()
    if total_size == 0:
        print("Wrong!")
    else:
        if total_size % 2 == 1:
            median = float(max_heap.peek())
        else: 
            median = (max_heap.peek() - min_heap.peek()) / 2.0
        
        if median == int(median):
            print(int(median))
        else:
            print(median)