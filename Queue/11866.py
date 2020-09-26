# https://www.acmicpc.net/problem/11866

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, K = map(int, input().split())
    result = list()
    sequence = [num + 1 for num in range(N)]
    pointer = -1

    for _ in range(N):
        pointer = (pointer + K) % N

        while sequence[pointer] == 0:
            pointer = (pointer + 1) % N

        result.append(sequence[pointer])
        sequence[pointer] = 0

        print(sequence)

    print(result)