def power(x, n):
    # Please add your code here
    if n == 0:
        return 1
    if n % 2 == 0:
        # even
        return power(x, n/2)*power(x, n/2)
    else:
        # odd
        return power(x, n//2)*power(x, n//2)*x
