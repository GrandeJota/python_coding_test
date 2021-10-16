n = input()
if len(n)%2 == 0:
    print(int(n[:len(n)//2]) + int(n[len(n)//2:]))
else:
    if n[1] == '0':
        print(int(n[:2]) + int(n[2:]))
    else:
        print(int(n[:1]) + int(n[1:]))