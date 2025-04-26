import random
lst = [random.randrange(0,31) for _ in range(0,50)]
print("Original List",lst)
n=1
unique_lst=[]
for i in lst:
    if(i not in unique_lst):
        unique_lst.append(i)
print("Unique List:",unique_lst)
