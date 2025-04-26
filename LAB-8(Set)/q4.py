s = {"Avi","Aalay","Boss","Batsman"}
a,b = set(),set()
for i in s:
    if(i.startswith("A") or i.startswith("a")):
        a.add(i)
    elif(i.startswith("B") or i.startswith("b")):
        b.add(i)
        
print("Set A:",a)
print("Set B:",b)
