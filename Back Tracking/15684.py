#  https://www.acmicpc.net/problem/15684


def dfs(cur, cnt, num):
    global res
    if cnt == num:
        if check():
            res = min(res, cnt)
        return
    if cur == size:
        return
    x = cur % (N - 1) + 1
    y = cur // (N - 1) + 1
    if graph[y][x] == [0,0] and graph[y][x + 1] == [0,0]:
        graph[y][x][1] = x + 1
        graph[y][x + 1][0] = x
        dfs(cur + 1, cnt + 1,  num)
        graph[y][x][1] = 0
        graph[y][x + 1][0] = 0
    dfs(cur + 1, cnt, num)


def check():
    for col in range(1, N + 1):
        sink = col
        for row in range(1, H + 1):
            if graph[row][col][0] != 0:
                col = graph[row][col][0]
            elif graph[row][col][1] != 0:
                col = graph[row][col][1]
        if sink != col:
            return False
    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M, H = map(int,input().split())
    graph = [[[0, 0] for col in range(N + 1)] for row in range(H + 1)]
    size = (N - 1) * H
    res = 4

    for _ in range(M):
        a, b = map(int,input().split())
        graph[a][b][1] = b + 1
        graph[a][b + 1][0] = b

    for num in range(4):
        dfs(0, 0, num)

    print(-1 if res > 3 else res)
