import random
s = set()
p = set()
while(len(s)<10):
    s.add(random.randrange(15,46))
print(s)
count=0

# l = list(s)
# for i in l:
#     if(i<30):
#         count+=1
# l=[i for i in l if i<35]    
# s = set(l)    

for i in s:
    if(i>35):
        p.add(i)


print("Total no. of Numbers less than 30:",count)
print("Set after all operations:",s-p)

