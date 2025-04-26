import sys,os,shutil
if os.path.exists('.\\mydir'):
    print("Directory exists")
else:
    os.mkdir('.\\mydir')
if os.path.exists("D:\\sem2\\eee\\Unit-III - Polyphase.pdf"):
    shutil.copyfile("D:\\sem2\\eee\\Unit-III - Polyphase.pdf",'.\\mydir\\mydirUnit-III - Polyphase.pdf')
    print("File successfully copied")
else:
    print("File Doesn't exists")



