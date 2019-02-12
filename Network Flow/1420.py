#  https://www.acmicpc.net/problem/1420


def init():
    source, sink = 0, 0
    source_x, source_y, sink_x, sink_y = 0, 0, 0, 0
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 'K':
                source += (M * row + col) * 2
                source_x = col
                source_y = row
            elif graph[row][col] == 'H':
                sink += (M * row + col) * 2 + 1
                sink_x = col
                sink_y = row
    for row in range(N):
        for col in range(M):
            match((row * M + col) * 2, (row * M + col) * 2 + 1, 1)
            for r, c in zip(dx, dy):
                next_row = row + r
                next_col = col + c
                if N <= next_row or next_row < 0 or M <= next_col or next_col < 0:
                    continue
                if graph[next_row][next_col] == '#':
                    continue
                match((row * M + col) * 2 + 1, (next_row * M + next_col) * 2, inf)
    for r, c in zip(dx, dy):
        x = sink_x + c
        y = sink_y + r
        if x == source_x and y == source_y:
            return source, sink, False
    return source, sink, True


def match(u, v, c):
    adj[u].append(v)
    adj[v].append(u)
    capacity[u].append(c)
    capacity[v].append(0)
    flow[u].append(0)
    flow[v].append(0)


def bfs(way):
    queue = __import__('collections').deque()
    queue.append(source)
    while queue:
        cur = queue.popleft()
        for index, nxt in enumerate(adj[cur]):
            if capacity[cur][index] > flow[cur][index] and way[nxt] == -1:
                way[nxt] = cur
                queue.append(nxt)
                if nxt == sink:
                    return


def solve():
    total = 0
    while True:
        way = [-1 for _ in range(size)]
        bfs(way)
        if way[sink] == -1:
            break
        cur = sink
        while cur != source:
            nxt = way[cur]
            flow[nxt][adj[nxt].index(cur)] += 1
            flow[cur][adj[cur].index(nxt)] -= 1
            cur = nxt
        total += 1
    return total


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1,0,-1,0)
    dy = (0,1,0,-1)
    inf = 2100000000

    N, M = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    size = N * M * 2
    adj = [[] for _ in range(size)]
    capacity = [[] for _ in range(size)]
    flow = [[] for _ in range(size)]
    sink, source, can = init()

    print(solve() if can else -1)