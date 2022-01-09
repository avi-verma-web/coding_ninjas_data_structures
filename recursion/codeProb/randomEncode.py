def encode(s):
    # Write your code here.
    if len(s) == 0 or len(s) == 1:
        return s+"1"
    otpt = encode(s[1:])
    if s[0] == s[1]:
        return s[0]+str(1+int(otpt[1]))+otpt[2:]
    else:
        return s[0]+"1"+otpt


print(encode("aabbbcccdd"))
