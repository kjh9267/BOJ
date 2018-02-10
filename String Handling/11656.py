a = raw_input()
b = [a[i:]for i in range(len(a))]
for i in xrange(len(b)):
    print sorted(b)[i]