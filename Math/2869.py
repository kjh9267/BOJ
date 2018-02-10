a, b, v = map(int,raw_input().split())
day = 1
up = a - b
v -= a
if v > 0:
    if v % up == 0:
        day += v/up
    else:
        day += v/up + 1
print day