n, w, h, l = list(int(i) for i in input().split())
a = (w//l)*(h//l)
print(n if a > n else a)