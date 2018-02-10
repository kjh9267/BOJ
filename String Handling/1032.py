a = [raw_input() for i in range(input())]
b = ''
c = [[0 for u in range(len(a))] for i in range(len(a[0]))]
for i in range(len(a[0])):
    for u in range(len(a)):
        c[i][u] = a[u][i]
for i in range(len(c)):
    if len(set(c[i])) == 1:
        b += c[i][0]
    else:
        b += '?'
print b