times = eval("list(int(i) for i in input().split()), "*3)

for i in range(3):
    secs = (times[i][3] * 3600 + times[i][4] * 60 + times[i][5]) - (times[i][0] * 3600 + times[i][1] * 60 + times[i][2])
    print(secs//3600, secs//60%60, secs%60)