ans = set()
for i in range(1,21):
    if i % 2 == 0 and i % 3 !=0:
        ans.add(i)
print(ans)