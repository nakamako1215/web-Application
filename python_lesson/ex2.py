data = {
    'Alice': {'math': 80, 'english': 90},
    'Bob': {'math': 75, 'english': 85},
    'Carol': {'math': 90, 'english': 95}
}
d = {}
for name,subject in data.items():
    total = sum(subject.values())
    num = len(subject.values())
    d[name] = total/num
    
print(d)
"""
def func(**kwargs):
    print(kwargs)
func(key1=1,key2=2,key3=3)
func(**d)
"""
def func2(func,ls):
    print(func)
    return func(ls)

print(func2(len,[1,5,3,2]))

func_ls = [len,sum,max,min]
numbers = [1,5,3,2]

for func in func_ls:
    print(func2(func,numbers))