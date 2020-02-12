# https://www.acmicpc.net/problem/1012

from sys import stdin
from collections import deque


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def solve():
    cnt = 0
    for row in range(N):
        for col in range(M):
            if not grid[row][col]:
                continue
            if visited[row][col]:
                continue
            bfs(Node(col, row))
            cnt += 1
    return cnt


def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node.y][node.x] = True

    while queue:
        cur = queue.popleft()

        for diff_x, diff_y in zip(dx, dy):
            next_x = cur.x + diff_x
            next_y = cur.y + diff_y
            if not (0 <= next_y < N and 0 <= next_x < M):
                continue
            if not grid[next_y][next_x]:
                continue
            if visited[next_y][next_x]:
                continue
            visited[next_y][next_x] = True
            queue.append(Node(next_x, next_y))


if __name__ == '__main__':
    input = stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())
        grid = [[False for _ in range(M)] for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            x, y = map(int, input().split())
            grid[y][x] = True

        print(solve())