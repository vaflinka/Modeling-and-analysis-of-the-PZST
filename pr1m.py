def longestOnes(nums):
    max_count = 0
    current = 0

    for value in nums:
        if value == 1:
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0

    return max_count

print(longestOnes([1,1,0,1,1,1]))  
print(longestOnes([1,0,1,1,0,1]))  
print(longestOnes([0,0,0]))        
print(longestOnes([1,1,1,1]))      