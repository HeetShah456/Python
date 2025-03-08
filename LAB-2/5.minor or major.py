#minor or major 
def minor_or_major(age):
       x="major" if age>18 else "minor"
       return x
a=int(input("Enter the age:"))
print("The person is:",minor_or_major(a))