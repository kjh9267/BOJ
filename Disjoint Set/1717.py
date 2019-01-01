import sys


def find(cur):
    if parent[cur] < 0:
        return cur
    parent[cur] = find(parent[cur])
    return parent[cur]


def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    elif parent[a] > parent[b]:
        parent[b] += parent[a]
        parent[a] = b
    else:
        parent[a] += parent[b]
        parent[b] = a


n, m = map(int,sys.stdin.readline().split())
parent = [-1 for _ in range(n+1)]

for _ in range(m):
    op, a, b = map(int,sys.stdin.readline().split())

    if op is 0:
        merge(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")