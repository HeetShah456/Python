def prime(n,i=2):
  if(n%i==0):
      if(i==n):
          print(i,end="")
          return
      print(i," ",end="")
      prime(n//i,2)
  else:
      prime(n,i+1)
n=int(input("Enter the num:"))
(prime(n))