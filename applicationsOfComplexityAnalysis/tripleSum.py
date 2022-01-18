
def tripletSum(a, n, num):
    a = sorted(a)
    count = 0
    for i in range(n-2):
        start = i+1
        end = n-1
        while start < end:
            if a[i]+a[start]+a[end] == num:
                count = count+1
                break
            elif a[i]+a[start]+a[end] < num:
                start = start+1
            elif a[i]+a[start]+a[end] > num:
                end = end-1
    return count


a = [2, -5, 8, -6, 0, 5, 10, 11, -3]
print(tripletSum(a, len(a), 10))
