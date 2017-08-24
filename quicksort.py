"""
An implementation of the quicksort algorithm
"""

def quicksort(array, low, high):
    """This functions represents a quicksort algorithm to sort a list.
    """
    if low < high:
        pivot = partition(array, low, high)
        # recursively call the quicksort function
        quicksort(array, low, pivot)
        quicksort(array, pivot + 1, high)



def partition(array, low, high):
    """This function implements the partition entity.
    Partition works this way:
        it reorders the sub-array of elements less that the pivot to
    come before it,
        and reorders the sub-array of elements whose values are greater than
        the pivot to come after it.
    """
    temp = 0
    pivot = array[low]
    i = low - 1
    j = high + 1

    while array[i] < pivot:
        i += 1
    while array[j] > pivot:
        j -= 1

    if i >= j:
        return j
    # swap array[i] with array[j]
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
