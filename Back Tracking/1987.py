# https://www.acmicpc.net/problem/1987


def dfs(x, y, depth):
    res[0] = max(res[0], depth)

    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        if not (0 <= next_x < C and 0 <= next_y < R):
            continue
        next_value = grid[next_y][next_x]
        if visited[next_value]:
            continue
        visited[next_value] = True
        dfs(next_x, next_y, depth + 1)
        visited[next_value] = False


if __name__ == '__main__':
    dx = (1, 0, -1, 0)
    dy = (0 , 1, 0, -1)
    input = __import__('sys').stdin.readline
    R, C = map(int, input().split())
    grid = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(R)]
    visited = [False for _ in range(26)]
    visited[grid[0][0]] = True
    res = [1]
    dfs(0, 0, 1)
    print(res[0])