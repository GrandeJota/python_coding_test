nums = list(map(int, input().split()))
nums.sort(reverse=True)
print(*nums)
print(nums.pop(), nums.pop(), nums.pop())