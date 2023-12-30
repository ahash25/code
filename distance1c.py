import math
def distance(x1,x2,y1,y2):
    dx=x2-x1
    dy=y2-y1
    print("the value of dx is",dx)
    print("the value of dy is",dy)
    d=(dx**2+dy**2)
    dist=math.sqrt(d)
    return dist
x1=float(input("enter the first number:"))
x2=float(input("enter the second number:"))
y1=float(input("enter the third number:"))
y2=float(input("enter the fourth number:"))
z=distance(x1,x2,y1,y2)
print("the distance between two points are",z)
