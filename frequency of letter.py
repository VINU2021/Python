name1= input("enter a word : ")
print("the given word is ",name1)
# using dict.get() to get count of each element in string 
res = {}
  
for i in name1:
    res[i] = res.get(i, 0) + 1
  
# printing result 
print (" count of all character in given word is ",name1," :\n"
                                             +  str(res))
