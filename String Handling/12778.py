import sys

t = int(sys.stdin.readline())

for _ in range(t):
    m, k = sys.stdin.readline().split()
    s = sys.stdin.readline().split()

    if k == 'C':
        print(" ".join(list(map(str,map(lambda x : x - 64,map(int,map(ord,s)))))))
    else:
        print(" ".join(map(str,list(map(chr,map(lambda x : x + 64,map(int,s)))))))