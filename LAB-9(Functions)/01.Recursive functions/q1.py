d = {"lower":0,"upper":0}

def count_lower_upper(str):
    for i in str:
        if(i.islower()):
            d["lower"] += 1
        elif(i.isupper()):
            d["upper"] += 1
            
count_lower_upper(str = input("Enter a String:"))
print(d)
