def palindrome(s):
    lis = list(s)
    r = list(reversed(lis))

    if lis == r: return True
    else: return False
