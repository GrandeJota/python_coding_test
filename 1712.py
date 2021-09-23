a, b, c = list(int(i) for i in input().split())

print('-1' if c-b <= 0 else a//(c-b)+1)