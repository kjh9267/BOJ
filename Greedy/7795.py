if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    T = int(input())

    for _ in range(T):
        result = 0
        N, M = map(int, input().split())
        A = list(sorted(map(int, input().split())))
        B = list(sorted(map(int, input().split())))
        b_idx = 0
        b = B[0]

        for a in A:
            while b_idx < M:
                b = B[b_idx]
                if a <= b:
                    break
                b_idx += 1
            result += b_idx

        print(result)
