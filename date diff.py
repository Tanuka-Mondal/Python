from datetime import date

d1 = int(input("Enter the 1st day in this manner: yyyy,mm,dd: "))
d2 = int(input("Enter the 2nd day in this manner: yyyy,mm,dd: "))

dt1 = d1.split(",")
dt2 = d2.split(",")

D1 = tuple(dt1)
D2 = tuple(dt2)

date1 = date(d1)
date2 = date(d2)
delta = date2 - date1
print(delta.days)