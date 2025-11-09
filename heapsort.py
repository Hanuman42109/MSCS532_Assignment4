"""
heapsort.py
In-place Heapsort implementation (max-heap) with a small CLI for quick tests.
"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    import random, time, sys
    size = 1000
    if len(sys.argv) > 1:
        try:
            size = int(sys.argv[1])
        except:
            pass
    arr = [random.randint(0, size*10) for _ in range(size)]
    t0 = time.time()
    heapsort(arr)
    t1 = time.time()
    print("Sorted? ", all(arr[i] <= arr[i+1] for i in range(len(arr)-1)))
    print("n =", size, "time = {:.6f}s".format(t1-t0))
