n = int(input())

table = 0
add_n = 2
for i in range(n):
    table += add_n
    if(i%2 == 0 and i != 0):
        add_n += 1
print(table)