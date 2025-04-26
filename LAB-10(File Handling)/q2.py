f = open('data.csv','r')
d={}
l = f.readlines()
n = l[0].strip().split(',')
for i in range(0,len(n)):
    d[n[i]]=[]

# for i in range(1, len(l)):
#     m = l[i].strip().split(',')  
#     for j in range(len(n)):
#         d[n[j]].append(m[j])
for i in range(1, len(l)):
    m = l[i].strip().split(',')
    total = sum([int(m[j]) for j in range(-3, 0)])  # sum of last 3 elements (subject marks)

    for j in range(len(m)):
        d[n[j]].append(m[j])
    
    # Add total to 'Total' key
    d['Total'].append(str(total))  #
print(d)
f.close()
