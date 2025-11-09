"""
scheduler_sim.py
A small scheduler simulation that uses the PriorityQueue.
Simulates arrival of tasks and processes them by priority.
"""

import time
import random
from priority_queue import PriorityQueue, Task

def simulate(num_tasks=20):
    pq = PriorityQueue()
    now = time.time()
    for i in range(num_tasks):
        # random priority [0,100)
        prio = random.randint(0, 100)
        t = Task(task_id=f"task{i}", priority=prio, arrival_time=now + i*0.1)
        pq.insert(t)
    processed = []
    while not pq.is_empty():
        task = pq.extract_max()
        processed.append(task)
    return processed

if __name__ == "__main__":
    proc = simulate(30)
    for t in proc:
        print(t)
