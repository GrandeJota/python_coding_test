h, m = map(int, input().split())
d = int(input())

print((h+(m+d)//60)%24, (m+d)%60)