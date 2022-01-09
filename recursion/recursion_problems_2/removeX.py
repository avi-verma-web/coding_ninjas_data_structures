def removeX(s):
    if len(s) == 0:
        return s
    output = removeX(s[1:])
    if s[0] == 'x':
        return output
    else:
        return s[0]+output


s = "xabcdxgxsd"

print(removeX(s))