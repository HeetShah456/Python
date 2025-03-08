#area and perimeter of the triangle
def check(a,p):
    if a>p:
        return "greater"
    else:
        return "lesser"
a,b,c=int(input("Enter the first side:")),int(input("Enter the second side:")),int(input("Enter the third side:"))
p=a+b+c
s=p/2
a=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area is",check(a,p),"than the perimeter")