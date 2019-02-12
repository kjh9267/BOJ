def init(u, v, c):
    graph[u].append(v)
    graph[v].append(u)
    capacity[u].append(c)
    capacity[v].append(0)
    flow[u].append(0)
    flow[v].append(0)


def bfs():
    queue = __import__('collections').deque()
    queue.append(0)
    level[0] = 0
    while queue:
        cur = queue.popleft()
        for index, nxt in enumerate(graph[cur]):
            if level[nxt] == -1 and capacity[cur][index] > flow[cur][index]:
                level[nxt] = level[cur] + 1
                queue.append(nxt)
    return level[sink - 1] != -1


def dfs(cur, f):
    if cur == sink - 1:
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

    N, M = map(int,input().split())
    sink = N + M + 2
    graph = [[] for _ in range(sink)]
    capacity = [[] for _ in range(sink)]
    flow = [[] for _ in range(sink)]
    inf = float('inf')
    total = 0

    for person in range(1, M + 1):
        data = list(map(int,input().split()))[1:]
        for d in data:
            init(person, N + d, 1)

    for index in range(1, N + 1):
        init(0, index, 2)

    for index in range(N + 1, sink - 1):
        init(index, sink - 1, 1)

    while True:
        level = [-1 for _ in range(sink)]
        if not bfs():
            break
        work = [0 for _ in range(sink)]
        while True:
            f = dfs(0, inf)
            if not f:
                break
            total += f
    print(total)