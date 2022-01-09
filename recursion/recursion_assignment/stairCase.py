def stairCase(n):
    if (n==1):
        return 1
    if (n==2):
        return 2
    if (n==3):
        return 4
    return stairCase(n-1)+stairCase(n-2)+stairCase(n-3)
n = 5
print(stairCase(n))