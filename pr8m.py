def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1


print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))