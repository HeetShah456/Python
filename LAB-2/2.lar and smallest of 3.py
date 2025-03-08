#largest and smallest of 3
def largest_and_smalest(a,b,c):
    if a>b:
        if a>c:
            largest=a
            if b>c:
                smallest=c
            else:
                smallest=b
        else:
            largest=c
            smallest=b
            
        
    else:
        if b>c:
            largest=b
            if a>c:
                smallest=c
            else:
                smallest=a
        else:
            largest=c
            smallest=a
    return largest,smallest     
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))        
d=largest_and_smalest(a,b,c)
print("largest:",d[0],"smallest:",d[1])
        