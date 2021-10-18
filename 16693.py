a, p1 = list(int(i) for i in input().split())
r, p2 = list(int(i) for i in input().split())

if a/p1 > r**2*3.14159265358979323846/p2:
    print("Slice of pizza")
else:
    print("Whole pizza")