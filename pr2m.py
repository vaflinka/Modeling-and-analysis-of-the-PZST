def countEvenDigitNumbers(nums):
    count = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            count += 1
    return count


print(countEvenDigitNumbers([12, 345, 2, 6, 7896]))
print(countEvenDigitNumbers([555, 901, 482, 1771]))