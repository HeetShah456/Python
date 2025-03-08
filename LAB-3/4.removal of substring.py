def removal(s,s1):
    if s1 in s:
        s=s.replace(s1,"")
        return s
    else:
        return "The removal is not possible"
s=input("Ente the main string:")
s1=input("Enter the string to be removed:")
print(removal(s,s1))