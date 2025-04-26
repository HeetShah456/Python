import os,sys,shutil

if(os.path.exists('.\\fread.txt')):
    print("File exists..")
else:
    print("File from which we have to read the content doesn't exists")

fw = open('.\\fwrite.txt','w+')
fr = open('.\\fread.txt','r')

ch = fr.read(1)
while(ch!=''):
    if(ch.islower()):
        ch = ch.upper()
    fw.write(ch)
    ch = fr.read(1)
print("Process Done")
fw.close()
fr.close()
