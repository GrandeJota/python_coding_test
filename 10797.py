dict_n = {}
n = int(input())
dict_n = {n:0}
cars = list(int(i) for i in input().split())

for i in cars:
    dict_n[i] = dict_n[i] + 1 if dict_n.get(i) != None else 1

print(dict_n[n])
# print(input().count(n))