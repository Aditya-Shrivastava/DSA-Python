"""
    Algorithm:
    selectionSort(array, size)
        repeat (size - 1) times
        set first unsorted element as minimum
        for each of the unsorted elements
            if element < currentMinimum
                set element as new minimum
        swap minimum with first unsorted position
    end

    Time Complexity: O(n^2)

"""
def selectionSort(array, size):
    for i in range(size):
        
        minimum_index = i
        for j in range(i + 1, size):
            if array[j] < array[minimum_index]:
                minimum_index = j

        array[i], array[minimum_index] = array[minimum_index], array[i]

    print (array)

array = [1, 6, 5, 20, 30, 5]
size = len(array)
selectionSort(array, size)
