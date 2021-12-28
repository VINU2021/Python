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
