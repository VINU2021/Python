import operator
s = input("enter a string :")
def most_frequent_letter(string):
  d = dict()
  for letter in s:
     if letter not in d:
        d[letter] = s.count(letter)
# Sort dictionary by values
  ordered_answer = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
  print (ordered_answer)
print(most_frequent_letter(s))
