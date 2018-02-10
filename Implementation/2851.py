a = [input() for i in range(10)]
c = []
x = []
y = [0]*10
for u in range(10):
    x.append(sum(a))
    a.pop(len(a)-1)
for i in range(len(x)):
    y[i] = abs(x[i] - 100)
if y.count(min(y)) == 2:
    for i in range(len(y)):
        if min(y) == y[i]:
            c.append(i)
    if x[c[0]] > x[c[1]]:
        print x[c[0]]
    else:
        print x[c[1]]
else:
    print x[y.index(min(y))]