mins, bats = list(int(i) for i in input().split())

if bats >= 20:
    c_bats = 100-bats
    bpmins = c_bats/mins
    print((bats-20)/bpmins + 40/bpmins)
else:
    bpmins = (80+(20-bats)*2)/mins
    print(bats/(bpmins/2))