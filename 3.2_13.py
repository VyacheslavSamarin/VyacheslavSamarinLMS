s = [input() for _ in range(int(input()))] # список продов которые может заготовить этот черт
a, z, z1 = int(input()), set(), []
for _ in range(a):
    for j in range(int(input())):
        z.add(input())
for i in range(len(s)):
    z1.append(s[i]) if s[i] not in z else False
z1 = sorted(z1)
print(*z1, sep='\n')







