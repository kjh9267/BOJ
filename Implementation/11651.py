import sys

for i in sorted([list(reversed(list(map(int,sys.stdin.readline().split())))) for _ in range(int(sys.stdin.readline()))]):
    print(i[1],i[0])