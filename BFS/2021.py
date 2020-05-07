# https://www.acmicpc.net/problem/2021


def bfs():
    queue = __import__('collections').deque()
    queue.append(start)

    visited = [False for _ in range(L + 1)]

    for node in adj[start]:
        visited[node] = True

    cnt = 0
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
                            return cnt

    return -1


if __name__ == '__main__':
    inf = float('inf')
    input = __import__('sys').stdin.readline
    N, L = map(int, input().split())
    adj = [set() for _ in range(N + 1)]
    lines = [set() for _ in range(L + 1)]

    for idx in range(1, L + 1):
        lines[idx] |= set(map(int, input().split()[:-1]))

    start, end = map(int, input().split())

    for line, stations in enumerate(lines):
        for station in stations:
            adj[station].add(line)

    print(0 if adj[start] & adj[end] else bfs())