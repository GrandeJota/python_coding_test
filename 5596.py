mings = list(int(i) for i in input().split())
mans = list(int(i) for i in input().split())

print(max(sum(mings), sum(mans)))