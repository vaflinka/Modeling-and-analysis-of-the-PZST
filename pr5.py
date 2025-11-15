def myPow(x, n):
    if n == 0:
        return 1.0

    if n < 0:
        return 1 / myPow(x, -n)

    if n % 2 == 0:
        half = myPow(x, n // 2)
        return half * half

    return x * myPow(x, n - 1)


print(myPow(2.00000, 10))   
print(myPow(2.10000, 3))   
print(myPow(2.00000, -2))   