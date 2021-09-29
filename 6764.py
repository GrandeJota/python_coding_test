a, b, c, d = list(eval("int(input()), "*4))

# if depths[0]*4 == sum(depths):
#     print("Fish At Constant Depth")
# else:
#     if depths == sorted(depths) and depths[0] != depths[1] and depths[1] != depths[2] and depths[2] != depths[3]:
#         print("Fish Rising")
#     elif depths == sorted(depths, reverse=True) and depths[0] != depths[1] and depths[1] != depths[2] and depths[2] != depths[3]:
#         print("Fish Diving")
#     else:
#         print("No Fish")
if a < b < c < d:
    print('Fish Rising')
elif a > b > c > d:
    print('Fish Diving')
elif a == b == c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')