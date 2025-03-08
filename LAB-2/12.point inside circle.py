#point inside or outside the circle
import math
def point_inside_circle(x,y):
    if math.sqrt(x**2+y**2)<1:
        return "inside"
    elif math.sqrt(x**2+y**2)==1:
        return "on the circle"
    else:
        return "outside"
a=float(input("Enter the x coord:"))
b=float(input("Enter the y coord:"))
print("The point is",point_inside_circle(a,b))
