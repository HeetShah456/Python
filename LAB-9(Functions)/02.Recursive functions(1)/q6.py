def avg(lst,i,sum):
    if(i==len(lst)):
        print(sum/len(lst))
        return
    sum += lst[i]
    avg(lst,i+1,sum)


lst = [1,2,3]
avg(lst,0,0)    