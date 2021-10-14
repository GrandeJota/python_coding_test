a, b, c = list(eval("int(input()), "*3))
print(min(a*2+c*2, min(a*4+b*2, b*2+c*4)))