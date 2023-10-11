a = input().split()
c = [{} for _ in range(len(a))]
for i in range(len(a)):
    x = bin(int(a[i]))[2:]
    c[i]["digits"] = len(x)
    c[i]["units"] = x.count('1')
    c[i]["zeros"] = x.count('0')
print(c)