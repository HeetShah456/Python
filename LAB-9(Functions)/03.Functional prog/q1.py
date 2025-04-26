def fun():
    print("1")
def disp():
    print("2")
def msg():
    print("3")

lst = [fun,disp,msg]
for i in lst:
    i()

'''
def fun():
  return 1
def disp():
  return 2
def msg():
  return 3

lst = [fun(),disp(),msg()]
for i in lst:
  print(i)
'''
  
