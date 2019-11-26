# https://www.acmicpc.net/problem/18115

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = list(map(int, input().split()))
    res = __import__('collections').deque()
    top = 0
    bottom = N - 1

    for num, skill in zip(range(1, N + 1), reversed(data)):
        if skill == 1:
            res.appendleft(num)
        elif skill == 2:
            top = res.popleft()
            res.appendleft(num)
            res.appendleft(top)
        else:
            res.append(num)

    print(' '.join(map(str,res)))