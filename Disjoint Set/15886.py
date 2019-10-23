# https://www.acmicpc.net/problem/15886


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    if parent[x] > parent[y]:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x
    return False


def dfs(x):
    if data[x] == 'E':
        xx = x + 1
    else:
        xx = x - 1
    if not (0 <= xx < N):
        return
    if not merge(x, xx):
        dfs(xx)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    parent = [-1 for _ in range(N)]
    data = list(input().rstrip())
    res = 0

    for idx in range(N):
        dfs(idx)

    for value in parent:
        if value < 0:
            res += 1

    print(res)