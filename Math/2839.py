n = input()
x = []
for i in range(n):
    for j in range(n):
        if 3*i + 5*j == n:
            x.append(i+j)
if len(x) > 0:
    print min(x)
else:
    print '-1'