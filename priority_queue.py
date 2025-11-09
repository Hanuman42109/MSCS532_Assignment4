"""
priority_queue.py
A max-heap priority queue implementation using a list as the underlying container.
Includes a Task class and common heap operations: insert, extract_max, increase_key, is_empty.
"""

from dataclasses import dataclass

@dataclass
class Task:
    task_id: str
    priority: float
    arrival_time: float = None
    deadline: float = None
    metadata: dict = None

    def __repr__(self):
        return f"Task(id={self.task_id}, prio={self.priority}, arrival={self.arrival_time}, deadline={self.deadline})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def insert(self, task: Task):
        # O(log n)
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        # O(log n)
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_task = self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return max_task

    def increase_key(self, index, new_priority):
        # O(log n)
        if index < 0 or index >= len(self.heap):
            raise IndexError("index out of range")
        if new_priority < self.heap[index].priority:
            raise ValueError("new priority is smaller than current")
        self.heap[index].priority = new_priority
        self._sift_up(index)

    def find_index_by_id(self, task_id):
        for i, t in enumerate(self.heap):
            if t.task_id == task_id:
                return i
        return -1

    def is_empty(self):
        return len(self.heap) == 0

    def _sift_up(self, i):
        while i > 0 and self.heap[self._parent(i)].priority < self.heap[i].priority:
            p = self._parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def _sift_down(self, i):
        n = len(self.heap)
        largest = i
        left = self._left(i)
        right = self._right(i)
        if left < n and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(largest)

# Simple demo
if __name__ == "__main__":
    import time
    pq = PriorityQueue()
    tasks = [Task(f"T{i}", priority=float(i%5), arrival_time=time.time()) for i in range(10)]
    for t in tasks:
        pq.insert(t)
    print("Heap after inserts:", pq.heap)
    print("Extracting max:")
    while not pq.is_empty():
        print(pq.extract_max())
