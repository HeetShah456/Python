#divisibility by 10
def d_10(a):
    if a%5==0 and a%2==0:
        return ""
    else:
        return "not"
a=int(input("Enter the number:"))
print("The number is",d_10(a),"divisible by 10")