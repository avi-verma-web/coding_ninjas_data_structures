def checkAB(str):
    if len(str) == 0:
        return True
    if str[0] == 'a':
        if str[1:3] == 'bb':
            return checkAB(str[3:])
        else:
            return checkAB(str[1:])
    else:
        return False


print(checkAB("abc"))
