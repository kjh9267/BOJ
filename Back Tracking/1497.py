# https://www.acmicpc.net/problem/1497


def check(data, res):
    songs = 0
    cnt = 0

    for idx in data:
        songs |= guitar[idx]

    while songs > 0:
        cnt += 1
        songs &= (songs - 1)

    res[cnt] = min(res[cnt], len(data))


def dfs(cur, depth, target_depth, data, res):
    if depth == target_depth:
        check(data, res)
        return
    for idx in range(cur, N):
        dfs(idx + 1, depth + 1, target_depth, data + [idx], res)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int, input().split())
    inf = float('inf')
    guitar = list()
    res = [inf for _ in range(M + 1)]

    for idx in range(N):
        _, can = input().split()
        can = can.replace("Y", '1')
        can = can.replace("N", '0')
        guitar.append(int(can, 2))

    for target_depth in range(1, N + 1):
        dfs(0, 0, target_depth, list(), res)

    for idx in range(M, 0, -1):
        if res[idx] != inf:
            print(res[idx])
            exit()

    print(-1)