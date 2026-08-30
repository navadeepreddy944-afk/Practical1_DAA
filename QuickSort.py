def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


numbers = [10, 7, 8, 9, 1, 5]

print("Before sorting:", numbers)

sorted_numbers = quick_sort(numbers)

print("After sorting:", sorted_numbers)
