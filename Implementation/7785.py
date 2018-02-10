x = {}
y = []
for i in range(input()):
    a, b = raw_input().split()
    x[a] = b
for i,j in x.items():
    if j == 'enter':
        y.append(i)
for i in sorted(y)[::-1]:
    print i