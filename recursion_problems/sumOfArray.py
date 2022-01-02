

def asum(a):
    if len(a)==0:
        return 0
    else:
        sum=a[0]+asum(a[1:])
        return sum

        
        

# 1,1,2,3,5
a=[1,2,8,4,5]
print(asum(a))
