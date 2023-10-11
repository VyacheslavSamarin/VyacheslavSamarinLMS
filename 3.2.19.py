s, z = {}, []
for _ in range(int(input())):
    x = input().replace(':', '').replace(',','').split()
    #s[x[0]] = set(x[i] for i in range(1,len(x)))
    for i in range(1, len(x)):
        if x[i] not in s:
            s[x[i]] = set()
        s[x[i]].add(x[0])
c = []
for x, y in s.items():
    if len(list(y)) == 1:
        c.append(x)
print(*c, sep='\n')


