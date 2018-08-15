import sys

n, m = map(int,sys.stdin.readline().split())
test = list(map(int,sys.stdin.readline().split()))
student = [[-1,-i] for i in range(1,100001)]

for _ in range(m):
    x = list(sys.stdin.readline().split())

    for i in range(1,n+1):
        if student[int(x[0]) - 1][0] == -1:
            student[int(x[0]) - 1][0] = 0
        if x[i] == 'O':
            student[int(x[0]) - 1][0] += test[i-1]

student = sorted(student)

print(-student[-1][1], student[-1][0])