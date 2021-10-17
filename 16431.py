b = list(int(i) for i in input().split())
d = list(int(i) for i in input().split())
j = list(int(i) for i in input().split())

bm = min(abs(j[0]-b[0]), abs(j[1]-b[1])) + abs(abs(j[0]-b[0]) - abs(j[1]-b[1]))
dm = (abs(j[0]-d[0]) + abs(j[1]-d[1]))

if bm > dm:
    print('daisy')
elif bm < dm:
    print('bessie')
else:
    print("tie")