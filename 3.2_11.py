a = int(input())
s = {}
k = 1
b = set()
for _ in range(a):
    x = input()
    if x not in s:
        s[x] = []
        s[x].append(k)
    else:
        s[x].append(k)
    k += 1
    b.add(x)
b = list(b)
k = 0
n = {}
for i in range(len(b)):
    if len(s[b[i]]) > 1:
        n[b[i]] = len(s[b[i]])
n1 = sorted(n)
if len(n1) == 0:
    print('Однофамильцев нет')
else:
    for i in range(len(n1)):
        print(f'{n1[i]} - {n[n1[i]]}')
