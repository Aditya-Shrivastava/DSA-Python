"""
    Algorithm:
    mergeSort(arr[], left, right)

        find middle element and divide array into two halves
        middle = (left + right) / 2

        call mergeSort for both halves
        mergeSort(arr, left, middle)
        mergeSort(arr, middle + 1, right)

        merge the two halves sorted in previous steps
        merge(arr, left, middle, right)

    Time Complexity: O(nlogn)
"""

import sys
sys.setrecursionlimit(10**6)

def merge(left_array, right_array):
    sorted_array = []
    i, j = 0, 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            j += 1
    
    sorted_array += left_array[i:]
    sorted_array += right_array[j:]
    return sorted_array

def merge_sort(array):
    if len(array) == 1:
        return array
    
    middle = len(array)//2
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])
    return merge(left_array, right_array)
 


if __name__ == "__main__":
    array = [20, 30, 5, 70, 40, 1, 13, 8, 5]
    print (merge_sort(array))
