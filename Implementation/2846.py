n = input()
a = map(int,raw_input().split())
h = 0
b = []
if n > 1:
    for i in range(n-1):
        if a[i+1] > a[i]:
            h += a[i+1] - a[i]
        else:
            b.append(h)
            h = 0
    b.append(h)
    print max(b)
else:
    print 0