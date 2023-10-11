a = sorted(input().replace(';', '').split())
z = {}
d = {}
c = []
for x in a:
    z[x] = set()
    for i in range(1, int(x) + 1):
        if int(x) % i == 0:
            z[x].add(i)
for x, y in z.items():
    d[x] = []
    for x1, y1 in z.items():
        if len(y1 & y) == 1:
            d[x].append(int(x1))
    d[x] = sorted(d[x])
    if len(d[x]) == 0:
        del d[x]
    else:
        c.append(int(x))
for x in sorted(c):
    #print(f'{str(x)} - {d[str(x)]}')
    s = []
    for i in range(len(d[str(x)])):
        s.append(d[str(x)][i]) 
    print(x, '-', end=' ')
    print(*s, sep=', ')

