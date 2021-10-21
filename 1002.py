""" 터렛문제 :   두 원의 교점 수 찾기
                floating point가 부정확하므로 제곱에서 계산 유지
"""
t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = list(int(i) for i in input().split())
    d = (x1-x2)**2+(y1-y2)**2
    if (r1 - r2)**2 < d < (r1 + r2)**2:
        print(2)
    elif ((r1 + r2)**2 == d) or ((r1 - r2)**2 == d and d != 0):
        print(1)
    elif r1 == r2 and d == 0:
        print(-1)
    else:
        print(0)