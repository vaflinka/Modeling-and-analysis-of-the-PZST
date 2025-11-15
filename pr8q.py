from collections import deque

def constrainedSubsetSum(nums, k):
    dq = deque()
    dp = nums[:]
    best = nums[0]

    dq.append(0)

    for i in range(1, len(nums)):
        if dq and dq[0] < i - k:
            dq.popleft()

        dp[i] = nums[i] + max(0, dp[dq[0]])

        while dq and dp[dq[-1]] < dp[i]:
            dq.pop()
        dq.append(i)

        best = max(best, dp[i])

    return best


print(constrainedSubsetSum([10,2,-10,5,20], 2))
print(constrainedSubsetSum([-1,-2,-3], 1))
print(constrainedSubsetSum([10,-2,-10,-5,20], 2))