def pairStar(s):
    if len(s) == 1:
        return s
    if s[0] == s[1]:
        return s[0]+"*"+pairStar(s[1:])
    else:
        return s[0]+pairStar(s[1:])


s = "abcdd"
print(pairStar(s))
