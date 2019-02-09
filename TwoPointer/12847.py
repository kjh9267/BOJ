#  https://www.acmicpc.net/problem/12847

if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    add = sum(data[:M])
    res = add
    for i in range(M,N):
        add -= data[i-M]
        add += data[i]
        if res < add:
            res = add
    print(res)