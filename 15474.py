n, a, b, c, d = list(int(i) for i in input().split())
x = (n//a + (0 if n%a == 0 else 1))*b
y = (n//c + (0 if n%c == 0 else 1))*d
print(min(x, y))