unis = ['Soongsil', 'Korea', 'Hanyang']
pers = list(int(i) for i in input().split())
if sum(pers) < 100:
    print(unis[pers.index(min(pers))])
else:
    print("OK")