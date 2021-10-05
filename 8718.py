x, k = list(int(i) for i in input().split())

if (k+k*2+k*4) <= x:
    print(int((k+k*2+k*4) * 1000))
elif (k/2+k+k*2) <= x:
    print(int((k/2+k+k*2) * 1000))
elif (k/4+k/2+k) <= x:
    print(int((k/4+k/2+k) *1000))
else:
    print(0)