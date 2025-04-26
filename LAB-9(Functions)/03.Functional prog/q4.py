lst = ['madam','Python',"malayalam",str(12321)]
def palindrome(s):
    for i in range(0,len(s)-1//2):
        if(s[i]!=s[len(s)-1-i]):
            return False
    return True
l = filter(palindrome,lst)
print(list(l))
