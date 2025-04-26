f = open('data.csv','a+')

rlno = input("Enter your rollno :")

while(rlno):
    nm = input("Enter your name :")
    cp, maths, eee = input("Enter your marks of computer, maths and eee(seperated by comma) :").split(',')
    f.write(f'{rlno},{nm},{cp},{maths},{eee}\n')
    rlno = input("Enter your rollno :")
f.close()
