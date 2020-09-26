# https://www.acmicpc.net/problem/9020


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = 10_001
    T = int(input())
    is_prime = [True for _ in range(N)]
    sqrt = int(N ** (1 / 2))

    is_prime[0] = is_prime[1] = False
    for idx in range(2, sqrt + 1):
        if not is_prime[idx]:
            continue
        for num in range(idx + idx, N, idx):
            is_prime[num] = False

    for _ in range(T):
        N = int(input())

        for num in range(N // 2, -1, -1):
            if is_prime[num] and is_prime[N - num]:
                print(num, N - num)
                break
