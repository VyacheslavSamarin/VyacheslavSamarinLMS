a, z, n = ' ', {}, set()
while True:
    a = input()
    if a == '':
        break
    else:
        a = a.split()
    if a[0] not in z:
        z[a[0]] = []
    if a[1] not in z:
        z[a[1]] = []
    z[a[1]].append(a[0])
    z[a[0]].append(a[1])
    n.add(a[0])
    n.add(a[1])
s, n = {}, sorted(n)
for x, y in z.items():
    if x not in s:
        s[x] = set()
    for i in y:
        h = z[i]
        for i in range(len(h)):
            s[x].add(h[i])
        
    if x in s[x]:
        s[x].remove(x)
    s[x] = sorted(s[x])
for x, y in z.items():
    for i in range(len(y)):
        if y[i] in s[x]:
            s[x].remove(y[i])
for h in n:
    print(h + ':', end=' ')
    print(*s[h], sep=', ')
  





