def rev(num):
    num.reverse()
    num = int("".join(num))
    return num
x, y = map(list,raw_input().split())
print rev(list(str(rev(x) + rev(y))))