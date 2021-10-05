import math
k, w, m = list(int(i) for i in input().split())
print(math.ceil((w-k)/m))