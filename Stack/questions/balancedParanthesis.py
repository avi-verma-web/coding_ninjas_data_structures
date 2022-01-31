def isBalanced(expression) :
	#Your code goes here
    open="{[("
    close=")]}"
    stack=[]
    for i in expression:
        if i in open:
            stack.append(i)
        elif i in close:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    return False
print(isBalanced("(()())"))