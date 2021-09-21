import sys

x, y, a = (int(i) for i in sys.stdin.readline().split())

print(a//y, a%y)