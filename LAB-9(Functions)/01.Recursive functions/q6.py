def sq_cube(n):
    l=[]
    for i in range(1,n+1):
        l.append((i,i**2,i**3))
        return l

print(sq_cube(n = int(input("Enter a number:"))))
