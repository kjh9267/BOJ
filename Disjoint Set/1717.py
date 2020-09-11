# https://www.acmicpc.net/problem/1717


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
    if rank[a] < rank[b]:
        a, b = b, a
    parent[a] += parent[b]
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int, input().split())
    parent = [-1 for _ in range(N + 1)]
    rank = [0 for _ in range(N + 1)]

    for _ in range(M):
        op, a, b = map(int, input().split())

        if op == 0:
            merge(a, b)
        elif find(a) == find(b):
            print("YES")
        else:
            print("NO")