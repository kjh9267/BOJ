import sys

s = list(sys.stdin.readline().rstrip())
a = [chr(i) for i in range(97,123)]
res = list()

for i in a:
    try:
        res.append(str(s.index(i)))
    except:
        res.append('-1')

print(' '.join(res))