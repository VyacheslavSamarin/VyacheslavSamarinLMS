a = int(input())
s = {}
for _ in range(a):
    x = input().split()
    if x[1] not in s:
        s[x[1]] = []
    s[x[1]].append(x[0])
b = input()
print(*sorted(s[b]), sep='\n') if b in s else print('Таких нет')
