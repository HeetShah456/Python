str = input("Enter a string: ")
d = {}
f=1
for i in str:
    if i not in d.keys():
        d[i]=f
    else:
        d[i]=f+1
print(d)

