a = [raw_input() for i in range(input())]
b = input()
if b == 1:
    for i in a:
        print i
elif b == 2:
    for i in a:
        print i[::-1]
else:
    for i in range(len(a)-1,-1,-1):
        print a[i]