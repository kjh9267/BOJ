import sys
n, k = map(int,sys.stdin.readline().split())
a = [map(int,sys.stdin.readline().split()) for i in range(n)]
b = []
c = []
cnt = 1
for i in a:
    if i[0] == k:
        k = i
for i in range(n):
    if a[i][1] > a[a.index(k)][1]:
        cnt += 1
    elif a[i][1] == a[a.index(k)][1]:
        b.append(a[i])
for i in range(len(b)):
    if b[i][2] > b[b.index(k)][2]:
        cnt += 1
    elif b[i][2] == b[b.index(k)][2]:
        c.append(b[i])
for i in range(len(c)):
    if c[i][3] > c[c.index(k)][3]:
        cnt += 1
print cnt