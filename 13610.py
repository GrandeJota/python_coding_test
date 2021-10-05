l, h = list(int(i) for i in input().split())
print(h//(h-l) + (1 if h%(h-l) != 0 else 0))