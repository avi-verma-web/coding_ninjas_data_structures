

def replaceAwithB(s):
    if len(s) == 0:
        return s
    output = replaceAwithB(s[1:])
    if s[0] == 'a':
        return 'b'+output
    else:
        return s[0]+output


s = "aaaa"

print(replaceAwithB(s))
