a, z = int(input()), {}
for _ in range(a):
    x, y = input(), input()
    h = str(len(x)) + ' ' + str(len(y))
    if h not in z:
        z[h] = []
    b = [x, y]
    z[h].append(b)
print(z)
