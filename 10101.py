dicts = {}
angles = 0
for i in range(3):
    ind = int(input())
    angles += ind
    dicts[ind] = 1 if dicts.get(ind) == None else dicts[ind] + 1

if angles == 180:
    if len(dicts) == 1:
        print("Equilateral")
    elif  len(dicts) == 2:
        print("Isosceles")
    elif  len(dicts) == 3:
        print("Scalene")
else:
    print("Error")