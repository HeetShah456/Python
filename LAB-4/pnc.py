#pnc
import math
n=int(input("Enter the value of n:"))
r=int(input("Enter the value of r:"))
print("The value of the ncr is:",(math.factorial(n))/((math.factorial(n-r))*(math.factorial(r))))
print("The value of the npr is:",(math.factorial(n))/(math.factorial(n-r)))

