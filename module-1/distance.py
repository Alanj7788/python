#distance between 2 points 
from math import sqrt
x1=int(input("x1:"))
x2=int(input("x2:"))
y1=int(input("y1:"))
y2=int(input("y2:"))

d=sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

print(d)