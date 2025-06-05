s = int(input("=>"))

n = list(map(int,input("=>").split()))

nn = n[:s]

nn.sort(reverse = True)

print(nn[0])