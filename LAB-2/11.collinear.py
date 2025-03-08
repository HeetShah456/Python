#collinear points
def collinear(m1,m2):
    if m1==m2:
        return "collinear"
    else:
         return "non collinear"
a=[]
b=[]
c=[]
for i in range(3):
    x=int(input("Enter the x coordinate:"))
    y=int(input("Enter the y coordinate:"))
    if i<1:
        a.append(x)
        a.append(y)
    elif i<2:
        b.append(x)
        b.append(y)
    else:
        c.append(x)
        c.append(y)
m1=(a[1]-b[1])/(a[0]-b[0])
m2=(a[1]-c[1])/(a[0]-c[0])
print("The points are",collinear(m1,m2))