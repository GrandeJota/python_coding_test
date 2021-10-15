q1, p1, q2, p2 = list(int(i) for i in input().split())
tr = q1/p1*q2/p2/2
if tr == int(tr):
    print(1)
else:
    print(0)

p1, q1, p2, q2 = map(int, input().split())
res = p1/q1 * p2/q2 / 2
if int(res) == res:
    print(1)
else:
    print(0)