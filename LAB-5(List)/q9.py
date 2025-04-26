# 9.)Take two lists of numbers. Create third list of numbers for only those numbers from first list 
# which are not there in 2nd list (use list comprehension). 

lst1 = [1,2,34,56,88]
lst2 = [34,17,19,88]
lst3=[]

for i in lst1:
    if(i not in lst2):
        lst3.append(i)
print(lst3)

