import sys


def find(cur):
    if graph[cur] < 0:
        return cur
    graph[cur] = find(graph[cur])
    return graph[cur]


def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    elif a > b:
        graph[b] += graph[a]
        graph[a] = b

    else:
        graph[a] += graph[b]
        graph[b] = a


n, m = map(int,sys.stdin.readline().split())
graph = [-1 for _ in range(n+1)]

for _ in range(m):
    op, a, b = map(int,sys.stdin.readline().split())

    if op is 0:
        merge(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")