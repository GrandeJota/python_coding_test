from sys import stdin
ax, ay, az = list(int(i) for i in stdin.readline().split())
azbx, ayby, axbz = list(int(i) for i in stdin.readline().split())

print(azbx - az, ayby//ay, axbz - ax)