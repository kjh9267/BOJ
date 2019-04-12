# https://www.acmicpc.net/problem/17135


def dfs(cur, depth):
    if depth == 3:
        # print(case)
        check()
        return
    if cur == M:
        return
    dfs(cur + 1, depth)
    case.append(cur)
    dfs(cur + 1, depth + 1)
    case.pop()


def check():
    cnt = 0
    for _ in range(N):
        cnt += count_dead()
        down()
    for row, line in enumerate(temp):
        graph[row] = line[:]
    res.append(cnt)


def down():
    for idx in range(N - 1, 0, -1):
        graph[idx] = graph[idx - 1]
    graph[0] = [0 for _ in range(M)]


def count_dead():
    dead = [0 for _ in range(M)]
    kill = list()
    for arrow in case:
        candi = list()
        for row in range(N):
            for col in range(M):
                if graph[row][col] == 0:
                    continue
                dist = abs(col - arrow) + abs(row - N)
                if dist <= D:
                    candi.append((dist, col, row))
        if candi:
            candi = sorted(candi)
            dead[candi[0][1]] = 1
            kill.append(candi[0])
    for k in kill:
        graph[k[2]][k[1]] = 0
    return sum(dead)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M, D = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    temp = [[] for _ in range(N)]
    for row in range(N):
        temp[row] = graph[row][:]
    case = list()
    res = list()
    dfs(0, 0)
    print(max(res))