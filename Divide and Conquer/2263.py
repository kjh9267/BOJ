# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(999999999)


def dfs(in_left, in_right, post_left, post_right):
    if in_left > in_right:
        return
    if post_left > post_right:
        return

    root = post_order[post_right]
    pre_order.append(root)
    root_idx = in_order[root]

    dfs(in_left, root_idx - 1, post_left, post_left + (root_idx - in_left) - 1)
    dfs(root_idx + 1, in_right, post_left + (root_idx - in_left), post_right - 1)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    in_order = [0 for _ in range(N)]
    data = map(int, input().split())

    for idx, node in enumerate(data):
        in_order[node - 1] = idx

    post_order = list(map(lambda x: int(x) - 1, input().split()))
    pre_order = list()

    dfs(0, N - 1, 0, N - 1)

    print(' '.join(map(lambda x: str(x + 1), pre_order)))