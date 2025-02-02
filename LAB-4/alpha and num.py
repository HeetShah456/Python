#no. of alphabets and numbers
a=input("Enter any string:")
len=len(a)
count_num=0
count_alpha=0
for i in range(0,len):
    if a[i].isalpha()==True:
        count_alpha+=1
    elif a[i].isdigit()==True:
        count_num+=1
print(count_num,count_alpha)

