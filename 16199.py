y1, m1, d1 = list(int(i) for i in input().split())
y2, m2, d2 = list(int(i) for i in input().split())

print((y2-y1) if (m2 > m1) or ((m2 == m1) and d2 >= d1) else y2-y1-1)
print(y2-y1+1)
print(y2-y1)