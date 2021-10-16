n = int(input())
p = {}
if n > 0:
    nes = list(int(i) for i in input().split())
    for i in nes:
        p[i] = (i*(nes.count(i)/len(nes)))

if sum(p.values()) != 0:
    print(f"{sum(nes)/n/sum(p.values()):0.2f}")
else:
    print("divide by zero")