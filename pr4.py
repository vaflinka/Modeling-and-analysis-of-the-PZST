def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(2))  
print(climbStairs(3))  
print(climbStairs(4))  
print(climbStairs(5))  