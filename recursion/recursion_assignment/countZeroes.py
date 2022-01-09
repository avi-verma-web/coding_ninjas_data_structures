def countZero(n):
    if n < 10:
        if n == 0:
            return 1
        return 0
    elif n % 10 == 0:
        return 1+countZero(n//10)
    else:
        return countZero(n//10)



n = 560030
print(countZero(n))
