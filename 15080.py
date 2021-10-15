h1, m1, s1 = list(int(i) for i in input().split(":"))
h2, m2, s2 = list(int(i) for i in input().split(":"))
t1 = h1*3600+m1*60+s1
t2 = h2*3600+m2*60+s2
if t1 > t2:
    t = t2+86400 - t1
else:
    t = t2 - t1
print(t)