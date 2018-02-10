r, c = map(int,raw_input().split())
x = [raw_input() for i in range(r)]
a, b = map(int,raw_input().split())
for i in range(len(x)):
    x[i] += x[i][::-1]
x += x[::-1]
for i in range(len(x)):
    x[i] = list(x[i])
if x[a-1][b-1] == '.':
    x[a-1][b-1] = '#'
else:
    x[a-1][b-1] = '.'
for i in range(len(x)):
    print "".join(x[i])