# https://www.acmicpc.net/problem/11724


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        pass
    elif parent[x] > parent[y]:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N ,M = map(int,input().split())
    parent = [-1 for _ in range(N + 1)]
    res = 0

    for _ in range(M):
        U, V = map(int, input().split())
        merge(U, V)

    for i in range(1, N + 1):
        if parent[i] < 0:
            res += 1

    print(res)