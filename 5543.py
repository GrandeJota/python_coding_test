burgers = []
for i in range(3):
    burgers.append(int(input()))

c_b = []
ci_b = []
coke = int(input())
for i in range(3):
    c_b.append(burgers[i] + coke)

cide = int(input())
for i in range(3):
    ci_b.append(burgers[i] + cide)

print(min(min(c_b), min(ci_b)) - 50)
# *p,q,r=eval("int(input()),"*5)
# print(min(p)+min(q,r)-50)