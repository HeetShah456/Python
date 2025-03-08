def no_of_vowels(s):
    n=0
    l=['a','e','i','o','u']
    for i in l:
        n+=s.count(i)
        print(i,s.count(i))
    
s=input("enter the string:")
print(no_of_vowels(s))