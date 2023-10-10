s = {}
while True:
    x = input()
    if x == '':
        break
    else:
        x = x.split()
    for i in range(len(x)):
        if x[i] not in s:
            s[x[i]] = 1
        else:
            s[x[i]] += 1

for key,value in s.items():
    print(key,value)
