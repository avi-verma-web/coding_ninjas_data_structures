a = [14, 20, 30, 53]


def split(arr):
    # Implement Your Function here
    a3 = []
    a5 = []
    a = []
    for i in range(0, len(arr)):
        if arr[i] % 3 == 0 and arr[i] % 5 != 0:
            a3.append(arr[i])
        elif arr[i] % 5 == 0:
            a5.append(arr[i])
        else:
            a.append(arr[i])
    if sum(a3)==sum(a5) and len(a)==0:
        return True
    elif sum(a3)==sum(a5) and len(a)!=0:
        return False
    elif sum(a3)!=sum(a5) and len(a)==0:
        return False
    elif sum(a3)!=sum(a5) and len(a)!=0:
        diff=abs(sum(a3)-sum(a5))
        if sum(arr)==diff:
            return True
        else:
            return False


print(split(a))
