from sys import stdin
L, P = (int(i) for i in stdin.readline().split())
lp = L*P
x = list(int(i) for i in stdin.readline().split())
for a in x:
    print(a-lp, end=" ")