scores = eval("int(input()) ,"*5)
su = 0
for i in scores:
    su = su + (i if i >= 40 else 40)
print(su//5)