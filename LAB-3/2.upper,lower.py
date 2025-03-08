def upper_lower_toggle(s):
    s1=""
    print("Original string:",s)
    for i in s:
        if 65<=ord(i)<=90:
            s1+=chr(ord(i)+32)
        elif 97<=ord(i)<=122:
            s1+=chr(ord(i)-32)
    return s1
s=input("Enter the string:")
print(upper_lower_toggle(s))