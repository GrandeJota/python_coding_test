a, b, c, d, e = eval("int(input()), "*5)
t = ((-a * c) + d + (b * e) if a < 0 else (b * e + d) if a == 0 else (b - a) * e)
print(t)