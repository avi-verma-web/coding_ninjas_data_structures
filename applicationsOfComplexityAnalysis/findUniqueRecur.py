

def findUnique(a):
    d={}
    for ele in a:
        if ele in d:
            d[ele]=d[ele]+1
        else:
            d[ele]=1
    for i in d:
        if d[i]==1:
            return i
           


a=[2,4,7,2,7]

print(findUnique(a))