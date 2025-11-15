def replaceElements(arr):
    max_right = -1
    for i in range(len(arr) - 1, -1, -1):
        new_val = max_right
        if arr[i] > max_right:
            max_right = arr[i]
        arr[i] = new_val
    return arr


print(replaceElements([17, 18, 5, 4, 6, 1]))
print(replaceElements([400]))