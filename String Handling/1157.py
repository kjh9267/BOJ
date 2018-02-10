s = raw_input()
for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122:
        s = s.replace(s[i], chr(ord(s[i])-32))
a = list(set(s))
b = [0]*len(a)
for i in range(len(a)):
    b[i] = s.count(a[i])
if b.count(max(b)) >= 2:
    print '?'
else:
    print a[b.index(max(b))]