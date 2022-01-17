# You have been given an integer array/list(ARR) of size N 
# which contains numbers from 0 to (N - 2).
# Each number is present at least once. That is, if N = 5, 
# the array/list constitutes values ranging from 0 to 3,
# and among these, there is a single integer value that is present twice. 
# You need to find and return that duplicate number present in the array.


def findDuplicate(arr, n) :
    #Your code goes here
    sum=0
    for ele in arr:
        sum=sum+ele
    sumNatural=((n-2)*(n-1))//2
    return sum-sumNatural