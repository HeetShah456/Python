import random
list_odd = [random.randrange(1,100,2) for _ in range(0,5)]
list_even = [random.randrange(0,100,2) for _ in range(0,4)]

# list_odd[2] = list_even
# print(list_odd)

j=0
for i in range(2,6):
    list_odd.insert(i,list_even[j])
    j+=1
list_odd.sort(reverse=True)
print(list_odd)

