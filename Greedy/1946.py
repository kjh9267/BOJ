# https://www.acmicpc.net/problem/1946


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    T = int(input())

    for _ in range(T):
        cnt = 1
        N = int(input())
        people = list(sorted([tuple(map(int, input().split())) for _ in range(N)]))
        min_value = people[0][1]

        for idx in range(1, N):
            value = people[idx][1]
            if value < min_value:
                cnt += 1
            min_value = min(min_value, value)

        print(cnt)
