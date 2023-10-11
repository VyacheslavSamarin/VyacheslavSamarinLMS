s, b, z, c = [input() for _ in range(int(input()))], [], {}, []
for i in range(int(input())):
    vs = input()
    z[vs] = [] if vs not in z else False
    for j in range(int(input())):
        z[vs].append(input())
for x, y in z.items():
    f = 0
    for i in range(len(y)):
        if y[i] not in s:
            f = 1
            break
    c.append(x) if f == 0 else False
print(*sorted(c), sep='\n')
