def checkPalindrome(s):
    if len(s)==1 or len(s)==0:
        return True
    if s[0]!=s[-1]:
        return False
    else:
        return checkPalindrome(s[1:len(s)-1])