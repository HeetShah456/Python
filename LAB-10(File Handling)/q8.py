fr = open('D:\\Programming\\Python\\code\\fh\\repl.txt','r')
lines = fr.readlines()
fw = open('D:\\Programming\\Python\\code\\fh\\writerepl.txt','w')
for i in lines:
    if(' a ' in i or ' the ' in i or ' an ' in i):
        i = i.replace(' a ',' ')
        i = i.replace(' the ',' ')
        i = i.replace(' an ',' ')
    fw.write(i)
fr.close(),fw.close()

