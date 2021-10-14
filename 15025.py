a, b = list(int(i) for i in input().split())
print("Not a moose" if (a == 0 and b == 0) else f"Even {a*2}" if a == b else f"Odd {max(a,b)*2}")