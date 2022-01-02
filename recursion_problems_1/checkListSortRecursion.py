

def lsort(a):
    n=len(a)
    if n==0 or n==1:
        return True
    if a[0]>a[1]:
        return False
    else:
        return lsort(a[1:])
        
        

# 1,1,2,3,5
a=[1,2,8,4,5]
print(lsort(a))
