p1, s1 = list(int(i) for i in input().split())
s2, p2 = list(int(i) for i in input().split())
p, s = p1+p2, s1+s2
if p > s:
    print("Persepolis")
elif p < s:
    print("Esteghlal")
else:
    if p2 > s1:
        print("Persepolis")
    elif p2 < s1:
        print("Esteghlal")
    else:
        print("Penalty")
