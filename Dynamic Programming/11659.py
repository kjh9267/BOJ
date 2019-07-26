# https://www.acmicpc.net/problem/11659

if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    acc = [0 for _ in range(N + 1)]
    acc[1] = data[0]

    for i in range(2, N + 1):
        acc[i] = acc[i - 1] + data[i - 1]

    for _ in range(M):
        s, e = map(int,input().split())
        print(acc[e] - acc[s - 1])