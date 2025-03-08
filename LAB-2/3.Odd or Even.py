#odd and even 
def odd_even(n):
    x="Even" if n%2==0 else "Odd"
    return x
a=int(input("Enter the number:"))
print("The number is:",odd_even(a),sep="")