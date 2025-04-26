import random
lst = [random.randrange(0,20) for _ in range(0,20)]
print(lst)
n= int(input("Enter a number: "))
if(n in lst):
    for i in range(0,20):
        if(lst[i]==n):
            print(f"Position: {i}")
else:
    print(n,"is not in list")
