def checkRedundant(s):
    open = "{[("
    close = "}])"
    stack = []
    count=0
    for i in s:
        if i not in close:
            stack.append(i)
            count = count+1
        elif i in close:
            while stack[-1] not in open:
                stack.pop()
            stack.pop()
            if count == 0:
                return True
            else:
                count=0
    return False

s="(a+b)"
print(checkRedundant(s))
