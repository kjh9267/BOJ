#  https://www.acmicpc.net/problem/2003

if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    left, right, acc, res = 0, 0, 0, 0
    while True:
        if acc >= M:
            acc -= data[left]
            left += 1
        elif right == N:
            break
        else:
            acc += data[right]
            right += 1
        if acc == M:
            res += 1
    print(res)