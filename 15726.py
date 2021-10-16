a, b, c = list(int(i) for i in input().split())
print(int(max(a*b/c, a/b*c)))