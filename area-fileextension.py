-----AREA OF A CIRCLE -----

pi = 3.14
r = float(input("Enter the radius of a circle:"))
area = pi * r * r
print("Area of a circle = ",area)


----FILE EXTENSION------
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
