def power(a,b,i,res):
    if(i>b):
        print(res)
        return
    res = res*a
    power(a,b,i+1,res)
power(2,3,1,1)