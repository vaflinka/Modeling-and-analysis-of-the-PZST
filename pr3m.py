def sortedSquares(nums):
    res = []
    for x in nums:
        res.append(x * x)
    res.sort()
    return res


print(sortedSquares([-4, -1, 0, 3, 10]))  
print(sortedSquares([-7, -3, 2, 3, 11]))