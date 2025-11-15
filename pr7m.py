def checkIfExist(arr):
    seen = set()
    for x in arr:
        if 2*x in seen or (x % 2 == 0 and x//2 in seen):
            return True
        seen.add(x)
    return False


print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([3, 1, 7, 11]))