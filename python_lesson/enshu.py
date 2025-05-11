list1 = list(range(1,10))
print(list1)
s = "1 2 3 4 5 6 7 8 9"
list2 = list(map(int,s.split()))
print(list2)

list1.remove(2)
print(list1)