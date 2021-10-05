dict_r = {'W':0, 'L':0}
dict_r['W'] = eval("(dict_r['W'] + 1) if (input()=='W') else 0, "*6)
cnt = sum(dict_r['W'])
print(-1 if cnt == 0 else 3 if 1 <= cnt < 3 else 2 if 3 <= cnt < 5 else 1)