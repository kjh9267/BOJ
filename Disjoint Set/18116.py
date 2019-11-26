# https://www.acmicpc.net/problem/18116


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
    N = int(input())
    parent = [-1 for _ in range(10 ** 6 + 1)]

    for _ in range(N):
        data = input().split()

        if data[0] == 'I':
            merge(int(data[1]), int(data[2]))
        else:
            print(-parent[find(int(data[1]))])