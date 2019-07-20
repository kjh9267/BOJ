# https://www.acmicpc.net/problem/16948


def bfs(sy, sx, ey, ex):
    queue = __import__('collections').deque()
    visited = [[False for col in range(N)] for row in range(N)]
    queue.append((sx, sy))
    visited[sy][sx] = True
    cnt = 0
    while queue:
        size = len(queue)
        cnt += 1
        for _ in range(size):
            x, y = queue.popleft()
            for i, j in zip(dx, dy):
                next_x = x + i
                next_y = y + j
                if not (0 <= next_y < N and 0 <= next_x < N):
                    continue
                if visited[next_y][next_x]:
                    continue
                if next_x == ex and next_y == ey:
                    return cnt
                visited[next_y][next_x] = True
                queue.append((next_x, next_y))
    return -1


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (-1, 1, -2, 2, -1, 1)
    dy = (-2, -2, 0, 0, 2, 2)
    N = int(input())
    sy, sx, ey, ex = map(int,input().split())
    print(bfs(sy, sx, ey, ex))