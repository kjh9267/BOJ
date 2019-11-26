# https://www.acmicpc.net/problem/14618


def dijkstra():
    pq = __import__('queue').PriorityQueue()
    res = [inf for _ in range(N + 1)]
    pq.put((0, J))
    res[J] = 0

    while not pq.empty():
        dist, cur = pq.get()
        for nxt, cost in adj[cur]:
            if res[nxt] > dist + cost:
                res[nxt] = dist + cost
                pq.put((res[nxt], nxt))

    return res

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int,input().split())
    J = int(input())
    K = int(input())
    As = set(map(int,input().split()))
    Bs = set(map(int,input().split()))
    adj = [[] for _ in range(N + 1)]
    inf = float('inf')

    for _ in range(M):
        X, Y, Z = map(int,input().split())
        adj[X].append((Y, Z))
        adj[Y].append((X, Z))

    res = dijkstra()
    min_dist = inf
    color = ''

    for home, dist in enumerate(res):
        if min_dist > dist > 0 and (home in As or home in Bs):
            min_dist = dist

    for home, dist in enumerate(res):
        if dist == min_dist:
            if home in As:
                color = 'A'
            elif home in Bs and color == '':
                color = 'B'

    if color == '' or min_dist == inf:
        print(-1)
    else:
        print(color)
        print(min_dist)