def frequency(s):
    d={}
    for i in s.split():
        if(i in d):
            d[i]+=1
        else:
            d[i]=1

    return dict(sorted(d.items()))



s = "apple banana mango mango apple"
# s = input("Enter a string:")
print(frequency(s))
