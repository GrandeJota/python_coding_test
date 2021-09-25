m, a = list(int(i) for i in input().split())

if ((m+a)%2 == 0 and (m-a)%2 == 0) and m-a >= 0:
    print((m+a)//2, (m-a)//2)
else:
    print(-1)