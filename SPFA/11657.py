#  https://www.acmicpc.net/problem/11657


class Node:
    def __init__(self, nxt, cost):
        self.nxt = nxt
        self.cost = cost


def spfa():
    dist = [inf for _ in range(N)]
    inQ = [False for _ in range(N)]
    isCycle = [0 for _ in range(N)]
    queue = __import__('collections').deque()

    queue.append(0)
    dist[0] = 0
    inQ[0] = True
    isCycle[0] += 1

    while queue:
        cur = queue.popleft()
        inQ[cur] = False
        for node in graph[cur]:
            if dist[node.nxt] > dist[cur] + node.cost:
                dist[node.nxt] = dist[cur] + node.cost
                if not inQ[node.nxt]:
                    queue.append(node.nxt)
                    inQ[node.nxt] = True
                    isCycle[node.nxt] += 1
                    if isCycle[node.nxt] == N:
                        return -1
    for index, cost in enumerate(dist):
        if cost == inf:
            dist[index] = -1
    return '\n'.join(map(str,dist[1:]))


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')

    N, M = map(int,input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = map(int,input().split())
        graph[A-1].append(Node(B - 1, C))

    print(spfa())
