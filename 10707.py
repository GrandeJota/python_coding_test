x = int(input())
y = eval("int(input()), "*3)
total_w = int(input())

print(min(x*total_w, y[0] + (((total_w - y[1]) * y[2]) if (total_w - y[1]) >= 0 else 0)))