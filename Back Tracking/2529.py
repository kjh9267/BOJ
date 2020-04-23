# https://www.acmicpc.net/problem/2529


def dfs_all():
    for num in range(10):
        visited[num] = True
        dfs(0, num)
        visited[num] = False


def dfs(depth, num):
    if depth == K:
        check(num)
        return
    for idx in range(10):
        if visited[idx]:
            continue
        if data[depth] == '>' and num % 10 < idx:
            continue
        if data[depth] == '<' and num % 10 > idx:
            continue
        visited[idx] = True
        dfs(depth + 1, num * 10 + idx)
        visited[idx] = False


def check(num):
    global max_num, min_num
    max_num = max(max_num, num)
    min_num = min(min_num, num)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    K = int(input())
    data = input().split()
    visited = [False for _ in range(10)]
    max_num, min_num = 0, float('inf')

    dfs_all()
    print('0' + str(max_num) if len(str(max_num)) < K + 1 else max_num)
    print('0' + str(min_num) if len(str(min_num)) < K + 1 else min_num)
