""""
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
acut = 0
bcut = 0
ocut = 0
word = set(words)
lst = list(word)
print(lst)

for cut in range(len(words)):
    
    if lst[0] == words[cut]:
        ocut +=1 
    elif lst[1] == words[cut]:
        acut +=1
    elif lst[2] == words[cut]:
        bcut +=1
print(acut,bcut,ocut)
print(acut,bcut,ocut)
"""

from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(words)
print(count['apple'],count['orange'],count['banana'])
di = {'apple':count['apple'],'orange':count['orange'],'banana':count['banana']}
print(di)
print(di.keys())
print(di.values())
