import sys
a = sys.stdin.readline
for i in sorted([list(reversed(list(map(int,a().split())))) for _ in range(int(a()))]):
    print(i[1],i[0])