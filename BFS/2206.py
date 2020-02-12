# https://www.acmicpc.net/problem/2206


class Node:
    def __init__(self, x, y, cnt):
        self.x = x
        self.y = y
        self.cnt = cnt


def bfs():
    queue = __import__('collections').deque()
    visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    queue.append(Node(0, 0, 0))
    visited[0][0] = [1, 1]

    while queue:
        cur = queue.popleft()
        for diff_x, diff_y in zip(dx, dy):
            next_x = cur.x + diff_x
            next_y = cur.y + diff_y
            if not (0 <= next_x < M and 0 <= next_y < N):
                continue
            value = grid[next_y][next_x]
            if value == '0' and visited[next_y][next_x][cur.cnt] == -1:
                visited[next_y][next_x][cur.cnt] = visited[cur.y][cur.x][cur.cnt] + 1
                queue.append(Node(next_x, next_y, cur.cnt))
            elif value == '1' and cur.cnt == 0 and visited[next_y][next_x][1] == -1:
                visited[next_y][next_x][1] = visited[cur.y][cur.x][0] + 1
                queue.append(Node(next_x, next_y, 1))

    mini = min(visited[N - 1][M - 1])
    maxi = max(visited[N - 1][M - 1])
    return mini if mini != -1 else maxi


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N, M = map(int, input().split())
    grid = [input().rstrip() for _ in range(N)]

    print(bfs())