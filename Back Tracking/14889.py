#  https://www.acmicpc.net/problem/14889


def dfs(depth, cur, case):
    if depth == M:
        check(case)
        return
    if cur == N:
        return
    dfs(depth, cur + 1, case)
    case[cur] = True
    dfs(depth + 1, cur + 1, case)
    case[cur] = False


def check(case):
    start = 0
    link = 0
    for i, bool1 in enumerate(case):
        for j, bool2 in enumerate(case):
            if bool1 and bool2:
                start += graph[i][j]
            elif not bool1 and not bool2:
                link += graph[i][j]
    res.append(abs(start - link))


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    M = N // 2
    graph = [list(map(int,input().split())) for _ in range(N)]
    res = list()
    dfs(0, 0, [False for _ in range(N)])
    print(min(res))