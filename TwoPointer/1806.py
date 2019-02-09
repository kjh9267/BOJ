#  https://www.acmicpc.net/problem/1806

if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N, S = map(int,input().split())
    data = list(map(int,input().split()))
    left, right, acc, res = 0, 0, 0, N + 1

    while True:
        if acc >= S:
            acc -= data[left]
            left += 1
        else:
            if right < N:
                acc += data[right]
                right += 1
            elif right == N:
                break
        if acc >= S:
            res = min(res, right - left)
    print(res if res != N + 1 else 0)