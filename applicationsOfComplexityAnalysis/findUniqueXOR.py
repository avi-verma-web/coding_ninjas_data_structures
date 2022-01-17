

def findUnique(a):
    xor=0
    for ele in a:
        xor=xor^ele
    return xor

        
           


a=[2,4,7,2,7]

print(findUnique(a))