skills = sorted(list(int(i) for i in input().split()))
print(abs((skills[1]-skills[0]) - (skills[3]-skills[2])))