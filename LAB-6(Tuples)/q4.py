lst =[("apple",90),("orange",60),("grapes",30),("watermelon",100)]

sorted_lst=sorted(lst,key=lambda item:item[1],reverse=True)        
print(sorted_lst)