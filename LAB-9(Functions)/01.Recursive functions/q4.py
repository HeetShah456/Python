def sum_avg(s1,s2,s3,s4,s5):
    sum,avg=0,0
    sum = s1+s2+s3+s4+s5
    avg = sum/5
    return sum,avg


print("Enter Marks:")
s1=int(input("S1:"))
s2=int(input("S2:"))
s3=int(input("S3:"))
s4=int(input("S4:"))
s5=int(input("S5:"))
print(sum_avg(s1,s2,s3,s4,s5))