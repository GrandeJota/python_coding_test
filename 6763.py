lim = int(input())
lim = int(input()) - lim

if 0<lim<=20:
    f = 100
elif 20<lim<=30:
    f = 270
elif 30<lim:
    f = 500
else:
    f = 0

print(f"You are speeding and your fine is ${f}." if f != 0 else "Congratulations, you are within the speed limit!")
