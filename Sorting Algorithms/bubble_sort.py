"""
    Algorithm:
    
    bubbleSort(array)
        for i from 1 to indexOfLastUnsortedElement - 1
            if leftElement > rightElement
                swap leftElement and rightElement
    end

    optimisedBubbleSort(array)
        swapped = false
        for i from 1 to indexOfLastUnsortedElement - 1
            if leftElement > rightElement
                swap leftElement and rightElement
                swapped = true
    end

    Time Complexity: O(n^2)
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    print (array)


def optimisedBubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                if swapped == False:
                    break
    
    print (array)

array = [20, 5, 30, 50, 4, 2]
bubbleSort(array)
optimisedBubbleSort(array)