if __name__ =='__main__':
    input = __import__('sys').stdin.readline

    N = int(input())
    res = 0
    from itertools import combinations
    for i in range(1, 31):
        res += len(list(combinations(range(1,31), i)))
    print(res)