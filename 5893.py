# ins = int(input(), 2)
# print(format(ins*17, 'b'))
# # ins = input()
# al = 0

# for i in range(len(ins)):
#     al += int(ins[i])*2**(len(ins)-1-i)

# print(format(al*17, 'b'))

data = input()
n = 0
for i in data:
    n = n<<1
    n += (i == "1")
n *= 17
print(format(n, 'b'))