import datetime
d1 = (11,8,2006)
d2 = (8,11,2006)

d1 = datetime.date(d1[2],d1[1],d1[0])
d2 = datetime.date(d2[2],d2[1],d2[0])
d= d2-d1
print(abs(d.days))
