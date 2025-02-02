#prime,arm...
a=int(input("Enter any positive integer:"))
count=0
count_per=0
if a>2:
    for i in range(1,a+1):
        if a%i==0:
           
            count+=1
   
    if count>2:
        print("The number is composite.")
    else:
        print("The number is prime")
elif a==1:
    print("NEITHER PRIME NOR COMPOSITE")
else:
    print("The number is prime")
p=a
digit=len(str(a))
x=(a**2)%(10**(len(str(a**2))-1))
new_arm=0
new_pali=0
while p>0:
    rem=p%10
    new_arm=new_arm+rem**3
    new_pali=new_pali+rem*(10**(digit-1))
    p=p//10
    digit-=1
if new_arm==a:
    print("The number is armstrong.")
if new_pali==a:
    print("The number palindrome.")
if a==x:
    print("The number is automorphic")
for i in range(1,a+1):
    if a%i==0:
        count_per+=i
count_per-=a
if count_per==a:
    print("The number is perfect")




