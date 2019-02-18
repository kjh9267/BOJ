#  https://www.acmicpc.net/problem/1167


class Node:
    def __init__(self, nxt, cost):
        self.nxt = nxt
        self.cost = cost


def dfs(cur, find):
    for node in tree[cur]:
        if find != 0:
            return find
        if visited[node.nxt]:
            continue
        visited[node.nxt] = True
        find = dfs(node.nxt, find)
    if find != 0:
        return find
    return cur


def bfs(start):
    queue = __import__('collections').deque()
    queue.append(start)
    visited = [-1 for _ in range(V + 1)]
    visited[start] = 0

    while queue:
        cur = queue.popleft()
        for node in tree[cur]:
            if visited[node.nxt] != -1:
                continue
            visited[node.nxt] += visited[cur] + node.cost + 1
            queue.append(node.nxt)
    res = max(visited)
    return visited.index(res), res


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    V = int(input())
    tree = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]

    for _ in range(V):
        line = list(map(int,input().split()))[:-1]
        size = len(line)
        node = line[0]
        for index in range(1, size, 2):
            tree[node].append(Node(line[index], line[index + 1]))

    visited[1] = True
    start = dfs(1, 0)
    start = bfs(start)[0]
    print(bfs(start)[1])