# https://www.acmicpc.net/problem/5214


def bfs():
    queue = __import__('collections').deque()
    queue.append(start)

    visited = [False for _ in range(M + 1)]

    for node in adj[start]:
        visited[node] = True

    cnt = 1
    while queue:
        size = len(queue)
        cnt += 1

        for _ in range(size):
            cur_station = queue.popleft()
            for line in adj[cur_station]:
                for nxt_station in lines[line]:
                    for nxt_line in adj[nxt_station]:
                        if visited[nxt_line]:
                            continue
                        visited[nxt_line] = True
                        queue.append(nxt_station)
                        if end in lines[nxt_line]:
                            return cnt + 1

    return -1


if __name__ == '__main__':
    inf = float('inf')
    input = __import__('sys').stdin.readline
    N, K, M = map(int, input().split())
    start, end = 1, N
    adj = [set() for _ in range(N + 1)]
    lines = [set() for _ in range(M + 1)]

    for idx in range(1, M + 1):
        lines[idx] |= set(map(int, input().split()))

    for line, stations in enumerate(lines):
        for station in stations:
            adj[station].add(line)

    print(1 if start == end else 2 if adj[start] & adj[end] else bfs())