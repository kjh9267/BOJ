# https://www.acmicpc.net/problem/2795


def go(cur, cnt):
    global res
    if cnt >= res:
        return
    if cur == 2:
        back(cur, cnt + 1)
    for nxt in adj[cur]:
        if go_visited[nxt]:
            continue
        go_visited[nxt] = True
        go(nxt, cnt+1)
        go_visited[nxt] = False


def back(cur, cnt):
    global res
    if cnt >= res:
        return
    if cur == 1:
        res = cnt
        return
    for nxt in adj[cur]:
        if back_visited[nxt]:
            continue
        back_visited[nxt] = True
        if go_visited[nxt]:
            back(nxt, cnt)
        else:
            back(nxt, cnt + 1)
        back_visited[nxt] = False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int, input().split())
    adj = [list() for _ in range(N + 1)]
    go_visited = [False for _ in range(N + 1)]
    back_visited = [False for _ in range(N + 1)]
    go_visited[1] = True
    back_visited[2] = True
    res = N

    for _ in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)

    go(1, 0)
    print(res)