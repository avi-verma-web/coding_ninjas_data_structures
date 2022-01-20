def helper(arr, n, start, lsum, rsum):
 
    # If reached the end
    if (start == n):
        return lsum == rsum
 
    # If divisible by 5 then add
    # to the left sum
    if (arr[start] % 5 == 0):
        lsum += arr[start]
 
    # If divisible by 3 but not by 5
    # then add to the right sum
    elif (arr[start] % 3 == 0):
        rsum += arr[start]
 
    # Else it can be added to any of
    # the sub-arrays
    else:
 
        # Try adding in both the sub-arrays
        # (one by one) and check whether
        # the condition satisfies
        return (helper(arr, n, start + 1,
                lsum + arr[start], rsum) or
                helper(arr, n, start + 1,
                lsum, rsum + arr[start]));
 
    # For cases when element is multiple of 3 or 5.
    return helper(arr, n, start + 1, lsum, rsum)
 
# Function to start the recursive calls
def split(arr, n):
     
    # Initially start, lsum and rsum
    # will all be 0
    return helper(arr, n, 0, 0, 0)