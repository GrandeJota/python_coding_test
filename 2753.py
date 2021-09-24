years = int(input())

print('1' if (years%4 == 0 and years%100 != 0) or years%400 == 0 else '0')