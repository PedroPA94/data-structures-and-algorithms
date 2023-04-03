def binary_search(array, value):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == value:
            return mid

        if array[mid] > value:
            end = mid - 1

        if array[mid] < value:
            start = mid + 1

    return None
