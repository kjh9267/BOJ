# https://www.acmicpc.net/problem/17129


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def bfs(start_node):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    queue = __import__('collections').deque()
    queue.append(start_node)

    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[start_node.y][start_node.x] = 0

    while queue:
        current_node = queue.popleft()

        for diff_x, diff_y in zip(dx, dy):
            next_x = current_node.x + diff_x
            next_y = current_node.y + diff_y

            if is_out_of_bound(next_x, next_y):
                continue
            if is_wall(next_x, next_y):
                continue
            if is_visited(next_x, next_y, visited):
                continue
            visited[next_y][next_x] = visited[current_node.y][current_node.x] + 1
            queue.append(Node(next_x, next_y))

    return visited


def is_visited(next_x, next_y, visited):
    return visited[next_y][next_x] != -1


def is_wall(next_x, next_y):
    return grid[next_y][next_x] == wall


def is_out_of_bound(next_x, next_y):
    return next_x < 0 or next_x == M or next_y < 0 or next_y == N


def find_shortest_dist():
    shortest_dist = float('inf')

    for row in range(N):
        for col in range(M):
            grid_value = grid[row][col]
            dist_value = dist[row][col]
            if grid_value not in ('3', '4', '5'):
                continue
            if dist_value == -1:
                continue
            shortest_dist = min(shortest_dist, dist_value)

    return shortest_dist


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    air = '0'
    wall = '1'
    N, M = map(int, input().split())
    grid = [input().rstrip() for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if grid[row][col] == '2':
                dist = bfs(Node(col, row))

    shortest_dist = find_shortest_dist()

    if shortest_dist == float('inf'):
        print('NIE')
    else:
        print('TAK')
        print(shortest_dist)