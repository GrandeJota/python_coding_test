d, h, m = list(int(i)-11 for i in input().split())
t = d*24*60 + h*60 + m
print('-1' if t < 0 else t)