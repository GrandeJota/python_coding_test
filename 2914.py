from sys import stdin
import math

(EA, u) = (int(i) for i in stdin.readline().split())

print(math.ceil((u-0.99)*EA))