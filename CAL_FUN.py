--CALCULATOR--

input("select operation from the following : 1-add , 2-sub , 3-mult ,4- div :  " )
if x=='1':
 a=int(input("enter a number : "))
 b=int(input("enter a number : "))
 c=a+b
 print("the addition of given 2 number is ",c)
elif x=='2':
 a=int(input("enter a number : "))
 b=int(input("enter a number : "))
 c=a-b
 print("the subraction of given 2 number is ",a-b)
elif x=='3':
 a=int(input("enter a number : "))
 b=int(input("enter a number : "))
 c=a*b
 print("the multiplication of given 2 number is ",a*b)
elif x=='4':
 a=int(input("enter a number : "))
 b=int(input("enter a number : "))
 c=a/b
 print("the multiplication of given 2 number is ",a/b)
else:
 print("the given input is invalid")
 
 --FUNCTION WITH 3 PARAMETER---
 def areaoftriangle(x,y,z):
 p=x+y+z
 print("the perimeter if the triangle is : ",p)
 s=p/2
 print("the semi-perimeter of the triangle is : ",s)
 a=(s*(s-x)*(s-y)*(s-z))*0.5
 print("the area of the triangle is :",a)

print("area of a triangle ")
h=float(input("enter the 1st side of triangle : "))
b=float(input("enter the 2nd side of triangle : "))
w=float(input("enter the 3rd side of triangle : "))
areaoftriangle(h,b,w)
 
