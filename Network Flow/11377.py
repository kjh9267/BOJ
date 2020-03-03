# https://www.acmicpc.net/problem/11377


def init(u, v, c):
    graph[u].append(v)
    graph[v].append(u)
    capacity[u].append(c)
    capacity[v].append(0)
    flow[u].append(0)
    flow[v].append(0)


def bfs():
    queue = __import__('collections').deque()
    queue.append(source)
    level[source] = 0
    while queue:
        cur = queue.popleft()
        for index, nxt in enumerate(graph[cur]):
            if level[nxt] == -1 and capacity[cur][index] > flow[cur][index]:
                level[nxt] = level[cur] + 1
                queue.append(nxt)
    return level[sink] != -1


def dfs(cur, f):
    if cur == sink:
        return f
    temp = work[cur]
    for index in range(temp,len(graph[cur])):
        work[cur] = index
        nxt = graph[cur][index]
        if level[nxt] == level[cur] + 1 and capacity[cur][index] > flow[cur][index]:
            df = dfs(nxt, min(f, capacity[cur][index] - flow[cur][index]))
            if df > 0:
                flow[cur][index] += df
                flow[nxt][graph[nxt].index(cur)] -= df
                return df
    return 0


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M, K = map(int,input().split())
    source = 0
    sink = N + M + 1
    filtering = sink + 1
    size = filtering + 1
    graph = [list() for _ in range(size)]
    capacity = [list() for _ in range(size)]
    flow = [list() for _ in range(size)]
    inf = float('inf')
    total = 0

    init(source, filtering, K)
    for person in range(1, N + 1):
        init(filtering, person, 1)
        data = list(map(int,input().split()))[1:]
        for value in data:
            init(person, N + value, 1)

    for index in range(1, N + 1):
        init(source, index, 1)

    for index in range(N + 1, sink):
        init(index, sink, 1)

    while True:
        level = [-1 for _ in range(size)]
        if not bfs():
            break
        work = [0 for _ in range(size)]
        while True:
            f = dfs(source, inf)
            if not f:
                break
            total += f
    print(total)