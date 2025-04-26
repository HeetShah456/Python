s = set()

print("Enter five names:")
for i in range(0,5):
    n = input()
    s.add(n)

m = input("Enter name that needs to be modified:")
n = input("Enter new name:")
s.remove(m)
s.add(n)
print(s)

print("Enter two names to remove:")
a,b = input(),input()
s.discard(a), s.discard(b)
print("Final Set:",s)





