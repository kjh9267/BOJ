#  https://www.acmicpc.net/problem/16167


class Node:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def bfs():
    queue = __import__('collections').deque()
    queue.append(1)

    cnt = 1
    while queue:
        size = len(queue)
        cnt += 1
        for _ in range(size):
            cur = queue.popleft()
            for nxt in graph[cur]:
                if res[nxt.node] == res[cur] + nxt.cost:
                    queue.append(nxt.node)
                    if nxt.node == N:
                        return cnt


def dijkstra():
    pq = __import__('queue').PriorityQueue()
    pq.put(Node(1, 0))
    res = [inf for _ in range(N + 1)]
    res[1] = 0

    while not pq.empty():
        cur = pq.get()
        for nxt in graph[cur.node]:
            if res[nxt.node] > res[cur.node] + nxt.cost:
                res[nxt.node] = res[cur.node] + nxt.cost
                pq.put(Node(nxt.node, res[nxt.node]))
    return res


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, R = map(int,input().split())
    graph = [[] for _ in range(N + 1)]
    inf = float('inf')

    for _ in range(R):
        a, b, c, d, e = map(int,input().split())
        if e > 10:
            graph[a].append(Node(b, c + (e - 10) * d))
        else:
            graph[a].append(Node(b, c))

    res = dijkstra()
    if res[N] == inf:
        print("It is not a great way.")
    else:
        print(res[N], bfs())