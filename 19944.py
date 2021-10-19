n, m = list(int(i) for i in input().split())
if m <= 2:
    print("NEWBIE!")
elif 2 < m <= n:
    print("OLDBIE!")
else:
    print("TLE!")