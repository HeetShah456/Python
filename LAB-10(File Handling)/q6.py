f1 = open('1.txt','r')
f2 = open('2.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
f = open('3.txt','w+')
for i in range(0,max(len(l1),len(l2))):
    if i < len(l1):
        f.write(l1[i])
    if i < len(l2):
        f.write(l2[i])
f1.close()
f2.close()               












