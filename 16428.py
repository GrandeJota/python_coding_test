import sys
a, b = list(int(i) for i in sys.stdin.readline().split())
c, d = divmod(a, b)
if a != 0 and b < 0:
    c, d = c+1, a-c*b
print(c)
print(d)