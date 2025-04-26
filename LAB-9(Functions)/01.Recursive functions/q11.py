def create_list(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    l = list(l1.intersection(l2))
    return l 


l1 = [8,2,308,18,11]
l2 = [1,4,11,18,33]
print(create_list(l1,l2))

