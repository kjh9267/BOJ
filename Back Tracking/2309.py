#  일곱 난쟁이
#  https://www.acmicpc.net/problem/2309

input = __import__('sys').stdin.readline


def dfs(cur, data):
    global res
    if len(data) == 7 and sum(data) == 100:
        res = data
        return
    if cur == 9:
        return
    dfs(cur + 1, data + [nums[cur]])
    dfs(cur + 1, data)


if __name__ == '__main__':
    nums = sorted([int(input()) for _ in range(9)])
    res = list()
    dfs(0,list())
    print("\n".join(map(str,res)))