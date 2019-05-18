# https://www.acmicpc.net/problem/14919

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    m = int(input())
    nums = list(sorted(map(lambda x: int(x[2:] + '0'*(7 - len(x[2:]))), input().split())))
    divs = [i * 10000000 // m for i in range(1, m + 1)]
    pointer = 0
    cnt = 0
    for div in divs:
        for idx in range(pointer, len(nums)):
            if nums[idx] < div:
                cnt += 1
                pointer = idx + 1
            else:
                pointer = idx
                break
        print(cnt, end=' ')
        cnt = 0