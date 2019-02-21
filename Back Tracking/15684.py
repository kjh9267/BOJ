#  https://www.acmicpc.net/problem/15684


def dfs(cur, cnt, cases):
    if cur == size:
        return
    if cnt == 3:
        check(cases)
    x = cur % (N - 1)
    y = cur // (N - 1) + 1
    if graph[y][x] == 0:
        dfs(cur + 1, cnt + 1, cases + [[x, y, x + 1]])
    dfs(cur + 1, cnt, cases)


def check(cases):
    temp = deep_copy(graph)

    for col in range(1, N):
        sink = col
        for row in range(1, H + 1):
            if graph[row][col][0] != 0:
                col = graph[row][col]
            elif graph[row][col][1] != 0:
                col = graph[row][col]
        if sink != col:
            return False
    return True


def deep_copy():
    temp = [[[0, 0] for col in range(N + 1)] for row in range(H + 1)]
    for row in range(1, N + 1):
        for col in range(1, H + 1):
            for i in range(2):
                temp[row][col][i] = graph[row][col][i]
    return temp


def


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M, H = map(int,input().split())
    graph = [[[0, 0] for col in range(N + 1)] for row in range(H + 1)]
    size = (N - 1) * H

    for _ in range(M):
        a, b = map(int,input().split())
        graph[a][b][1] = b + 1
        graph[a][b + 1][0] = b

