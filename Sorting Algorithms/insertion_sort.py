"""
    insertion_sort(arr)
        mark first element as sorted
        for each unsorted element x
            extract the element x
            for j from lastSortedIndex down to 0
                if current element j > x
                    move sorted element to right by 1
            break loop and insert x here
    end

    Time Complexity: O(n^2)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        sorted_element = arr[i]
        j = i - 1
        while j >= 0 and sorted_element < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = sorted_element


if __name__ == "__main__":
    array = [20, 30, 5, 70, 40, 1, 13, 8, 5]
    print (array)
    insertion_sort(array)
    print (array)