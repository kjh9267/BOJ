# https://www.acmicpc.net/problem/1600


class Node:
    def __init__(self, x, y, cnt):
        self.x = x
        self.y = y
        self.cnt = cnt


def bfs():
    queue = __import__('collections').deque()
    visited = [[[-1 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    queue.append(Node(0, 0, 0))
    visited[0][0] = [0 for _ in range(K + 1)]

    while queue:
        cur = queue.popleft()
        for idx, diff in enumerate(zip(dx, dy)):
            next_x = cur.x + diff[0]
            next_y = cur.y + diff[1]
            if not (0 <= next_x < M and 0 <= next_y < N):
                continue
            if grid[next_y][next_x] == '1':
                continue
            if cur.cnt == K and idx >= 4:
                continue
            next_cnt = cur.cnt + (0 if idx < 4 else 1)
            if visited[next_y][next_x][next_cnt] != -1:
                continue
            visited[next_y][next_x][next_cnt] = visited[cur.y][cur.x][cur.cnt] + 1
            queue.append(Node(next_x, next_y, next_cnt))

    res = float('inf')
    for cnt in visited[N - 1][M - 1]:
        if cnt != -1 and cnt < res:
            res = cnt
    return res if res != float('inf') else -1


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0, 1, 1, -1, -1, 2, 2, -2, -2)
    dy = (0, 1, 0, -1, 2, -2, 2, -2, 1, -1, 1, -1)
    K = int(input())
    M, N = map(int, input().split())
    grid = [input().split() for _ in range(N)]

    print(bfs())