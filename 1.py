def partition(a, si, ei):
    pivot = a[si]
    count = 0
    for ele in a:
        if ele < pivot:
            count = count+1
    a[si+count], a[si] = a[si], a[si+count]
    pivot_index = si+count
    i = si
    j = ei
    while i < j:
        if a[i] < pivot:
            i = i+1
        elif a[j] >= pivot:
            j = j-1
        else:
            a[i], a[j] = a[j], a[i]
            i = i+1
            j = j-1
    return pivot_index


def quickSort(a, si, ei):
    if si >= ei:
        return
    if len(a)==1:
        return
    index = partition(a, si, ei)
    quickSort(a, si, index-1)
    quickSort(a, index+1, ei)


a = [2, 6, 8, 5, 4, 3,-9,8,-5]
quickSort(a, 0, len(a)-1)
print(a)
