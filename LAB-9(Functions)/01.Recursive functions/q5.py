def ispangram(str):
    s = set(str.upper())
    alpha = set()
    for i in range(65,91):
        alpha.add(chr(i))

    if(alpha.issubset(s)):
        return "str is pangram"
    else:
        return "str is not pangram"
        

# str = "The quick brown fox jumps over the lazy dog"
str = "Crazy Fredrick ought many very exquisite opal jewels"
print(ispangram(str))

