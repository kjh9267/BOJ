import sys

N, L, D = map(int,sys.stdin.readline().split())

for i in range(L,(L+5)*N,L+5):
    key = False
    for j in range(0,(L+5)*N + D,D):
        if i <= j < i + 5:
            print(j)
            key = True
            break
    if key:
        break
else:
    for i in range(0,(L+5)*N*1001,D):
        if i >= (L+5)*N:
            print(i)
            break