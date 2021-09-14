import sys
# a = map(int, sys.stdin.readline().rstrip().split())

# print(a)

# print(sum([x**2 for x in a])%10)

a = [x**2 for x in map(int, sys.stdin.readline().rstrip().split())]
print(sum(a)%10)