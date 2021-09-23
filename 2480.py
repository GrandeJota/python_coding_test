nums = list(int(i) for i in input().split())

dict_n = {}
max_n = {}
for i in nums:
    dict_n[i] = 1 if dict_n.get(i) == None else dict_n[i] + 1
    max_n[dict_n[i]] = i

print(max(dict_n) * 100 if max(max_n) == 1 else (10 + max_n[max(max_n)])*10**max(max_n))