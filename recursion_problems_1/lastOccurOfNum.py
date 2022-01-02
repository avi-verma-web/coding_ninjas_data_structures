

def lastOccurOfNum(a, num):
    if len(a) == 0:
        return -1
    output = lastOccurOfNum(a[1:], num)
    if output == -1:
        if a[0] == num:
            return 0
        else:
            return -1
    else:
        return output+1


# 1,1,2,3,5
a = [1, 2, 8, 4, 5, 8, 9, 6, 3, 8]
num = 8
print(lastOccurOfNum(a, num))
