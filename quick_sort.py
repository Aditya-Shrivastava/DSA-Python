"""
    Algorithm:
    left -> starting index, rihgt -> ending index
    quickSort(arr, left, right)
        if left < right
            find partition index 
            index = partitiono(arr, left, right)
            quickSort(arr, left, index - 1) -> left of partition index
            quickSort(arr, index + 1, right) -> right of partition index

    Time Complexity: O(nlogn)

"""


def partition(arr, left, right):
    pivot = arr[left]
    low = left + 1
    high = right

    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    
    arr[left], arr[high] = arr[high], arr[left]

    return high


def quick_sort(arr, left, right):
    if left > right: 
        return

    index = partition(arr, left, right)
    quick_sort(arr, left, index - 1)
    quick_sort(arr, index + 1, right)


if __name__ == "__main__":
    array = [20, 30, 5, 70, 40, 1, 13, 8, 5]
    print (array)
    quick_sort(array, 0, len(array) - 1)
    print (array)