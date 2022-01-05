def merge(a1, a2, a):
    i, j = 0, 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i = i+1
            k = k+1
        elif a1[i] >= a2[j]:
            a[k] = a2[j]
            j = j+1
            k = k+1
    while i < len(a1):
        a[k] = a1[i]
        i = i+1
        k = k+1
    while j < len(a2):
        a[k] = a2[j]
        j = j+1
        k = k+1


def mergeSort(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a)//2
    a1 = a[0:mid]
    a2 = a[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1, a2, a)


a = [2, 5, 6, 8, -7, 89, 24, 32]

mergeSort(a)
print(a)
