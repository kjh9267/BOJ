#  조세퍼스 문제
#  https://www.acmicpc.net/problem/1158

input = __import__('sys').stdin.readline


def cycle(pointer, seq, diff):
    nxt = pointer + diff - 1
    size = len(seq)
    return nxt % size


if __name__ == '__main__':
    N, M = map(int,input().split())
    sequence = list(range(1,N+1))
    res = list()
    pointer = 0

    for i in range(N):
        pointer = cycle(pointer, sequence, M)
        target = sequence[pointer]
        res.append(target)
        sequence.remove(target)

    print('<' + ', '.join(map(str,res)) + '>')