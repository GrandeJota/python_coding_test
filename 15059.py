a=[0, 0];b=[0, 0];c=[0, 0]
a[0], b[0], c[0] = list(int(i) for i in input().split())
a[1], b[1], c[1] = list(-int(i) for i in input().split())
print(abs(min(0, sum(a)) + min(0, sum(b)) + min(0, sum(c))))