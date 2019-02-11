#  https://www.acmicpc.net/problem/15892


def bfs():
    queue = __import__('collections').deque()
    queue.append(0)
    level[0] = 0
    while queue:
        cur = queue.popleft()
        for index, nxt in enumerate(graph[cur]):
            if level[nxt] is -1 and capacity[cur][index] > flow[cur][index]:
                level[nxt] = level[cur] + 1
                queue.append(nxt)
    return level[N-1] != -1


def dfs(cur,f):
    if cur == N-1:
        return f
    temp = work[cur]
    for i in range(temp,len(graph[cur])):
        work[cur] = i
        nxt = graph[cur][i]
        if capacity[cur][i] > flow[cur][i] and level[nxt] == level[cur] + 1:
            df = dfs(nxt,min(f, capacity[cur][i] - flow[cur][i]))
            if df > 0:
                flow[cur][i] += df
                flow[nxt][graph[nxt].index(cur)] -= df
                return df
    return 0


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N, M = map(int,input().split())
    graph = [[] for _ in range(N)]
    capacity = [[] for _ in range(N)]
    flow = [[] for _ in range(N)]
    inf = float('inf')
    total = 0

    for _ in range(M):
        a, b, c = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        capacity[a-1].append(c)
        capacity[b-1].append(c)
        flow[a-1].append(0)
        flow[b-1].append(0)

    while True:
        level = [-1 for _ in range(N)]
        if not bfs():
            break
        work = [0 for _ in range(N)]
        while True:
            f = dfs(0,inf)
            if not f:
                break
            total += f

    print(total)