import operator
string = input("enter a string :")
d = dict()
for letter in string:
    if letter not in d:
        d[letter] = string.count(letter)
# Sort dictionary by values
ordered_answer = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print (ordered_answer)
