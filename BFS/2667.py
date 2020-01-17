from sys import stdin
from collections import deque


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def bfs(x, y):
    queue = deque()
    queue.append(Node(x, y))
    visited[y][x] = True
    home_number = 0
    while queue:
        cur = queue.popleft()
        home_number += 1
        for diff_x, diff_y in direction:
            next_x = cur.x + diff_x
            next_y = cur.y + diff_y
            if not (0 <= next_y < N and 0 <= next_x < N):
                continue
            if grid[next_y][next_x] == '0':
                continue
            if visited[next_y][next_x]:
                continue
            queue.append(Node(next_x, next_y))
            visited[next_y][next_x] = True

    return home_number


if __name__ == '__main__':
    input = stdin.readline
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    N = int(input())
    grid = [input().rstrip() for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    res = list()

    for row in range(N):
        for col in range(N):
            if grid[row][col] == '0' or visited[row][col]:
                continue
            res.append(bfs(col, row))
            cnt += 1

    res.sort()
    print(cnt)

    for size in res:
        print(size)