def palindrome(str):
    str = str.lower().replace(" ","")
    s = str[::-1]
    
    if(s==str):
        return f"{str} is Palindrome"
    else:
        return f"{str} is not a Palindrome"

print(palindrome(str = input("Enter a string:")))

