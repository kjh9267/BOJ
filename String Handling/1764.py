import sys

n, m = map(int,sys.stdin.readline().split())
a = [sys.stdin.readline().rstrip() for _ in range(n)]
b = [sys.stdin.readline().rstrip() for _ in range(m)]
res = set(a).intersection(b)
print(len(res))

for i in sorted(res):
    print(i)