import math

d, h, w = list(int(i) for i in input().split())

print(int(math.sin(math.atan(h/w))*d), end=" ")
print(int(math.cos(math.atan(h/w))*d))