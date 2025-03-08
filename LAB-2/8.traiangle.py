#triangle
def triangle(s):
         if s==180:
                 return ("valid")
         else:
                 return ("not valid")
a,b,c=int(input("Enter the first angle:")),int(input("Enter the second angle:")),int(input("Enter the third angle:"))
s=a+b+c
print("The triangle is:",triangle(s))   