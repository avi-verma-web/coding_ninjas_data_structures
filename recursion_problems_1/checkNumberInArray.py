

def checkIfInArray(a, num):
    if len(a) == 0:
        return False
    else:
        if a[0] == num:
            return True
        else:
            return checkIfInArray(a[1:],num)


# 1,1,2,3,5
a = [1, 2, 8, 4, 5]
num = 9
print(checkIfInArray(a, num))
