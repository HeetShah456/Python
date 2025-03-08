#largest and smallest 
def largest_and_smallest(a,b):
    if a>b:
        return a,b
    else:
        b,a=a,b
        return a,b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=largest_and_smallest(a,b)
print(type(c))
print("largest:",c[0],"smallest:",c[1])