

def replacePi(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0:2] == 'pi':
        return "3.14"+replacePi(s[2:])
    else:
        return s[0]+replacePi(s[1:])


s = "pipipigpi"

print(replacePi(s))
