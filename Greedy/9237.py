# https://www.acmicpc.net/problem/9237


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = list(map(int,input().split()))
    data.sort(reverse=True)

    for idx in range(N):
        data[idx] += idx + 1

    print(max(data) + 1)