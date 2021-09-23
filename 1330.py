a, b = list(int(i) for i in input().split())

print('<' if a < b else '>' if a > b else '==')

#print('<') if a < b else print('>') if a > b else print('==')