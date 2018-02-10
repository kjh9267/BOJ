n, m = map(int,raw_input().split())
a = [raw_input() for i in range(n)]
for i in range(m):
    a.append(raw_input())
a = sorted(a)
b = []
for i in range(1,len(a)):
    if (a[i]) == (a[i-1]):
        b.append(a[i])
print len(b)
for i in b:
    print i