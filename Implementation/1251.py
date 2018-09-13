import sys


def convert(first,second):
    result.append(list(reversed(string[:first]))
                  + list(reversed(string[first:second]))
                  + list(reversed(string[second:])))


string = sys.stdin.readline().rstrip()
length = len(string)
result = list()

for i in range(1,length-1):
    for j in range(2,length):
        if i >= j:
            continue
        convert(i,j)

print(list(map(''.join,(sorted(result))))[0])