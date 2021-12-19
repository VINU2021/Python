n = int(input(" enter a number : "))
f0=0
f1=1
f2=0
print("the fibonacci series of given number is ")
if(n==0):
  print(f0)
elif(n==1):
  print(f0) 
  print(f1)
elif(n > 1):
  print(f0)
  print(f1)
  for i in range (2,n):
   f2=f0+f1
   f0=f1
   f1=f2
   print(f2)
else:
  print("the given value is invalid")
