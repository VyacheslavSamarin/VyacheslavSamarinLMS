a, z = int(input()), {}
for _ in range(a):
    x = input().split()
    y = x[1]
    x = x[0]
    h, f = x[:-1] + ' ' + y[:-1], [x, y] 
    if h not in z:
        z[h] = []
    z[h].append(f)
m = -1
for x in z.values():
    m = max(m, len(x))
print(m)


    
