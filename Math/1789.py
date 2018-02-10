s = input()
n = 0
a = 0
b = 1
while a <= s:
    a += b
    b += 1
    n += 1
if a == s:
    print n
else:
    print n-1