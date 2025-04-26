import random
lst = [random.randrange(-15,16) for _ in range(10)]
print(lst)
l = list(map(lambda x:x*x,lst))
print(l)