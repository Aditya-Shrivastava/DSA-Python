"""
    Algorithm:
    heap_sort(arr)
        heap_size = len(arr)
        build_max_heap(arr)
        for i from heap_size downto 1
            swap arr[0] and arr[i]
            heap_size = heap_size - 1
            max_heapify(arr, 1, heap_size)

    Time Complexity: O(nlogn)
"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    array = [20, 30, 5, 70, 40, 1, 13, 8, 5]
    print (array)
    heap_sort(array)
    print (array)
