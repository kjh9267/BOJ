s = raw_input()
a = map(int,s.replace('6','5').split())
b = map(int,s.replace('5','6').split())
print a[0] + a[1], b[0] + b[1]