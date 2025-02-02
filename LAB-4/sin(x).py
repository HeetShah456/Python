import math
x=int(input("Enter the value of the x in degrees:"))
x=x*(math.pi/180)
n=int(input("Enter the number of the terms:"))
value=0
for i in range(1,n+1):
    value=value+((x**((2*i)-1))/(math.factorial((2*i)-1)))*((-1)**(i-1))
print("The answer is :",value)
