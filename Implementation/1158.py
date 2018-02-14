n, m = map(int,raw_input().split())
a = m - 1
x = []
s = range(1,n+1)
while len(x) != n:
    x.append(s.pop(m-1))
    m += a
    if m > len(s):
        if len(s) != 0:
            if m % len(s) == 0:
                m = len(s)
            else:
                m = m % len(s)
        else:
            pass
x = str(x).replace('[','<')
print x.replace(']','>')
