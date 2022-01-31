
def reverseStack(s1, s2):
    if len(s1)<=1:
        return 
    while len(s1)!=1:
        s2.append(s1.pop())
    lastEle=s1.pop()
    while len(s2)!=0:
        s1.append(s2.pop())
    reverseStack(s1,s2)
    s1.append(lastEle)





s1=[1,2,3,4]
s2=[]
reverseStack(s1,s2)
print(s1)


