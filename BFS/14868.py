# https://www.acmicpc.net/problem/14868


def bfs():
    cnt = 1
    res = 0
    while queue:
        size = len(queue)
        for x, y in queue:
            for i, j in zip(dx, dy):
                xx = x + i
                yy = y + j
                cur = grid[y][x]
                if not (0 <= xx < N and 0 <= yy < N):
                    continue
                nxt = grid[yy][xx]
                if -1 < nxt != cur and merge(cur, nxt):
                    cnt += 1
                    if cnt == K:
                        return res
        res += 1
        for _ in range(size):
            x, y = queue.popleft()
            for i, j in zip(dx, dy):
                xx = x + i
                yy = y + j
                if not (0 <= xx < N and 0 <= yy < N):
                    continue
                if -1 < grid[yy][xx]:
                    continue
                grid[yy][xx] = grid[y][x]
                queue.append((xx, yy))


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if parent[x] > parent[y]:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x
    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1 ,0)
    dy = (0, 1, 0, -1)
    N, K = map(int, input().split())
    grid = [[-1 for _ in range(N)] for _ in range(N)]
    parent = [-1 for _ in range(K)]
    queue = __import__('collections').deque()

    for cnt in range(K):
        x, y = map(lambda x: int(x) - 1, input().split())
        grid[y][x] = cnt
        queue.append((x, y))

    print(bfs())