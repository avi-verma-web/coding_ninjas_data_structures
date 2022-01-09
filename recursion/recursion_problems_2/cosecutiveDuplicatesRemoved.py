
def cdr(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == s[1]:
        return cdr(s[1:])
    else:
        return s[0]+cdr(s[1:])


s = "aabbbccgddddioooop"

print(cdr(s))