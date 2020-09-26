# https://www.acmicpc.net/problem/15809


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if counts[x] < counts[y]:
        x, y = y, x
    counts[x] += counts[y]
    counts[y] = 0
    parent[y] = x


def fight(x, y):
    x = find(x)
    y = find(y)

    if counts[x] < counts[y]:
        x, y = y, x
    counts[x] -= counts[y]
    counts[y] = 0
    parent[y] = x


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int, input().split())
    counts = [int(input()) for _ in range(N)]
    parent = [idx for idx in range(N)]
    zero_cnt = 0
    res = list()

    for _ in range(M):
        O, P, Q = map(lambda x: int(x) - 1, input().split())

        if O == 0:
            merge(P, Q)
        if O == 1:
            fight(P, Q)

    counts.sort()

    for idx, value in enumerate(counts):
        if value == 0:
            zero_cnt += 1
        else:
            break

    print(N - zero_cnt)
    print(' '.join(map(str,counts[zero_cnt:])))