def secti(a, b):
    return a + b


def bubble_sort(arr): # [5, 3, 8, -2, 9]
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
    # Last i elements are already in correct position
        for j in range(0, n - i - 1):
        # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # return byl ve for-cyklu
    return arr

def error(param):
    if type(param) != int:
        raise TypeError