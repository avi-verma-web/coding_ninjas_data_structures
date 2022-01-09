
def binarySearch(a, num):
    if len(a) == 0:
        return -1
    mid = (0+len(a))//2
    if a[mid] == num:
        return a[mid]
    elif a[mid] < num:
        return binarySearch(a[mid+1:], num)
    elif a[mid] > num:
        return binarySearch(a[0:mid], num)


a = [1, 5, 20, 36, 47, 58, 69]
num = 696

print(binarySearch(a, num))
