import sys


def binary_search():
    first = 0
    last = trees[N-1]
    mid = (first + last) // 2
    while first <= last:
        temp = 0
        for tree in trees:
            if tree - mid > 0:
                temp += (tree - mid)
        if temp == M:
            return mid
        elif temp < M:
            last = mid - 1
        else:
            first = mid + 1
        mid = (first + last) // 2
    return mid


N, M = map(int,sys.stdin.readline().split())
trees = sorted(list(map(int,sys.stdin.readline().split())))
total = sum(trees)

print(binary_search())