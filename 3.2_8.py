a = int(input())
s = {}
for _ in range(a):
    x = input().split()
    for i in range(1, len(x)):
        if x[i] not in s:
            s[x[i]] = []
        s[x[i]].append(x[0])
b = input()
print(*sorted(s[b]), sep='\n') if b in s else print('Таких нет')
