#pythagorous triplets 
import math
n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i+1,n+1):
        k=math.sqrt(i**2+j**2)
        if k.is_integer()==True:
            print(i,j,int(k))