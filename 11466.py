ins = list(int(i) for i in input().split())
l = max(ins)
s = min(ins)
print(s if l >= 3*s else max(s/2, l/3))