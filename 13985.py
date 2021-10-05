ins = (list((i) for i in input().split()))
ans = []
ans.append(int(ins.pop()))
ins = list(int(i) for i in sorted(list((i) for i in ins))[1:len(ins)-1])
print("YES" if (sum(ins)==ans.pop()) else "NO")