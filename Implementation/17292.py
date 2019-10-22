# https://www.acmicpc.net/problem/17292


def dfs(cur, depth, cards):
    if depth == 2:
        pairs.append(cards)
        return
    for idx in range(cur, 6):
        if visited[idx]:
            continue
        visited[idx] = True
        dfs(idx, depth + 1, cards + data[idx])
        visited[idx] = False


def first_compare(pair):
    n1, c1, n2, c2 = pair
    n1 = int(n1, 16)
    n2 = int(n2, 16)
    res = 0
    if abs(n1 - n2) == 1 or abs(n1 - n2) == 14:
        res += 10
    if n1 == n2:
        res += 1
    return -res


def second_compare(pair):
    n1, c1, n2, c2 = pair
    n1 = int(n1, 16)
    n2 = int(n2, 16)
    res = 0
    if c1 == c2:
        res += 100000
    res += max(n1, n2) * 1000
    res += min(n1, n2) * 10
    if n1 >= n2 and c1 == 'b':
        res += 1
    elif n1 < n2 and c2 == 'b':
        res += 1
    return -res


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    data = input().rstrip().split(',')
    visited = [False for _ in range(6)]
    pairs = list()
    dfs(0, 0, '')
    print('\n'.join(sorted(pairs, key=lambda x: (first_compare(x), second_compare(x)))))