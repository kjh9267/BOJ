# https://www.acmicpc.net/problem/17822
import sys
sys.setrecursionlimit(999999999)


def rotate(idx, dir, cnt):
    for i in range(idx, N + 1, idx):
        if dir == 0:
            for _ in range(cnt):
                data[i].appendleft(data[i].pop())
        else:
            for _ in range(cnt):
                data[i].append(data[i].popleft())
    go()


def go():
    global sumi, total
    change = False
    for y in range(1, N + 1):
        for x in range(M):
            if dfs(x, y, data[y][x], 0):
                change = True

    if change:
        return
    if total > 0:
        avg = sumi / total
    else:
        return

    for y in range(1, N + 1):
        for x in range(M):
            if data[y][x] > avg:
                data[y][x] -= 1
                sumi -= 1
            elif data[y][x] < avg and data[y][x] != -1:
                data[y][x] += 1
                sumi += 1


def dfs(x, y, value, depth):
    global sumi, total
    change = False
    for i, j in zip(dx, dy):
        nxt_x = x + i
        xx = 0 if nxt_x == M else M - 1 if nxt_x == -1 else nxt_x
        yy = y + j
        if not (1 <= yy < N + 1):
            continue
        if data[yy][xx] == -1 or data[yy][xx] != value:
            continue
        if depth == 0:
            change = True
            data[y][x] = -1
        sumi -= data[yy][xx]
        total -= 1
        data[yy][xx] = -1
        dfs(xx, yy, value, depth + 1)
    if change:
        sumi -= value
        total -= 1
    return change


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N, M, T = map(int,input().split())
    deque = __import__('collections').deque
    data = [[]] + [deque(map(int, input().split())) for _ in range(N)]
    total = N * M
    sumi = 0

    for i in range(1, N + 1):
        sumi += sum(data[i])

    for _ in range(T):
        x, d, k = map(int,input().split())
        rotate(x, d, k)

    print(sumi)