def pairSum(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count = count + unordered_map[sum - arr[i]]

        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1

    return count


a = [1, 3, 6, 2, 5, 4, 3, 2, 4]
print(pairSum(a, len(a), 7))
