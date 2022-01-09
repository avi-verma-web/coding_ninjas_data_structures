#You can only use subtraction and addition for your calculation. No other operators are allowed.
# axb-> meaning add a b times-> (a+a+a+...b times)
from sys import setrecursionlimit
setrecursionlimit(10**6) 
def mul(a,b):
    if a>1000 or b>1000:
        return 0
    if a==0 or b==0 :
        return 0
    return a+mul(a,b-1)



a=6
b=5

print(mul(a,b))