x, y = eval("int(input()), "*2)
if x >= 0 and  y >= 0:
    print(1)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and 0 > y:
    print(4)
elif x < 0 and 0 < y:
    print(2)