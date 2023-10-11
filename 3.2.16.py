a = ' '
s = set()
while a != []:
    a = input().split()
    for i in range(len(a)):
        if a[i] == 'зайка':
            if i == 0:
                s.add(a[i + 1])
            elif i == len(a) - 1:
                s.add(a[i - 1])
            else:
                s.add(a[i - 1])
                s.add(a[i + 1])
print(*list(s), sep='\n')
