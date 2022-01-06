def stringToInterger(s):
    if len(s)==0:
        return 0
    if s[0]=='0':
        return stringToInterger(s[1:])
    else:
        return (int(s[0])*(10**len(s[1:])))+stringToInterger(s[1:])

        
s='00123'
print(stringToInterger(s))