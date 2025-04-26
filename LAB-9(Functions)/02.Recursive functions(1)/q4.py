def revList(lst,l,r):
    if(l>=r):
        print(lst)
        return
    temp=lst[l]
    lst[l]=lst[r]
    lst[r]=temp
    revList(lst,l+1,r-1)

lst = [1,2,3,4,5]
revList(lst,0,len(lst)-1)    