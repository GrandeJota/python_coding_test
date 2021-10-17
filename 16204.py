n, m, k = list(int(i) for i in input().split())
print(min(k, m)+min(n-k, n-m))