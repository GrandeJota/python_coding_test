n = int(input())
a = list(int(i) for i in input().split())
b = sorted(a)
for i in range(n):
    print(a.index(b[i]), end=" ")