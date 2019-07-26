# https://www.acmicpc.net/problem/17352


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


if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    parent = [-1 for _ in range(N)]
    for _ in range(N - 2):
        a, b = map(int,input().split())
        merge(a - 1, b - 1)
    for i in range(1, N):
        if find(0) != find(i):
            print('1 {}'.format(i + 1))
            break