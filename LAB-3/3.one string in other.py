def _find_(s,s1):
    if s1 in s:
        return True
    else:
        return False
s=input("Enter the main string:")
s1=input("Enter the string to be searched:")
print(_find_(s,s1))
