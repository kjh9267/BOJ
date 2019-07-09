# https://www.acmicpc.net/problem/3973

import sys
sys.setrecursionlimit(999999999)


def bfs(start):
    queue = __import__('collections').deque()
    queue.append(start)
    visited = [-1 for _ in range(N)]
    visited[start] = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            for nxt in tree[cur]:
                if visited[nxt] != -1:
                    continue
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)
    max_cnt = 0
    node = 0
    for idx, cnt in enumerate(visited):
        if max_cnt < cnt:
            max_cnt = cnt
            node = idx
    return max_cnt, node


if __name__ == '__main__':
    cnt = 0
    input = __import__('sys').stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        tree = [[] for _ in range(N)]
        for __ in range(N - 1):
            a, b = map(int,input().split())
            tree[a].append(b)
            tree[b].append(a)
        T_T, node = bfs(0)
        cnt, T_T = bfs(node)
        print(cnt//2 + 1 if cnt % 2 == 1 else cnt // 2)