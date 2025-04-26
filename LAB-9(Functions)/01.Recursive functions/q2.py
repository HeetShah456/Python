def compute(n):
    total=0
    sum=0
    for i in range(0,n):
        sum+=n*pow(10,i)
        total += sum
    return total


for n in range(4,8):
    print(f"For n = {n}",compute(n))                               


