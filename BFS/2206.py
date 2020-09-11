# https://www.acmicpc.net/problem/2206


class Node:
    def __init__(self, x, y, is_destroy):
        self.x = x
        self.y = y
        self.is_destroy = is_destroy


def bfs():
    queue = __import__('collections').deque()
    visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    queue.append(Node(0, 0, not_destroy))
    visited[0][0] = [1, 1]

    while queue:
        cur = queue.popleft()
        for diff_x, diff_y in zip(dx, dy):
            next_x = cur.x + diff_x
            next_y = cur.y + diff_y
            if not (0 <= next_x < M and 0 <= next_y < N):
                continue
            value = grid[next_y][next_x]
            if value == air and visited[next_y][next_x][cur.is_destroy] == -1:
                visited[next_y][next_x][cur.is_destroy] = visited[cur.y][cur.x][cur.is_destroy] + 1
                queue.append(Node(next_x, next_y, cur.is_destroy))
            elif value == wall and cur.is_destroy == not_destroy and visited[next_y][next_x][destroy] == -1:
                visited[next_y][next_x][destroy] = visited[cur.y][cur.x][not_destroy] + 1
                queue.append(Node(next_x, next_y, destroy))

    mini = min(visited[N - 1][M - 1])
    maxi = max(visited[N - 1][M - 1])
    return mini if mini != -1 else maxi


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    destroy = 1
    not_destroy = 0
    air = '0'
    wall = '1'
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N, M = map(int, input().split())
    grid = [input().rstrip() for _ in range(N)]

    print(bfs())