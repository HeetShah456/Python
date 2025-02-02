n=int(input("Enter the number of the terms:"))
a=0
b=1
for i in range(1,n-1):
    
    new=a+b
    a=b
    b=new
print("The nth term is:",new)